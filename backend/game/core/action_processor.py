import logging

from game.core.choice_service import AdventureChoiceService
from game.services.combat_service import CombatService
from game.services.dice_service import DiceService
from game.state.resolver.entity_resolver import EntityResolver
from game.state.runtime.runtime_player_service import RuntimePlayerService
from game_instances.services.llm.orchestrator.llm_service import LLMService
from game.npc.npc_service import NPCService

from game.state.runtime.models import Enemy as RuntimeEnemy
from world.models import Enemy as EnemyORM

from game.core.action_attack import AttackAction

logger = logging.getLogger(__name__)


class ActionProcessor:
    def __init__(self, state_manager, combat_service=None, resolver=None):
        self.state_manager = state_manager
        self.combat_service = combat_service or CombatService(DiceService())
        self.resolver = resolver or EntityResolver(state_manager)
        self.runtime_player_service = RuntimePlayerService(state_manager)
        self.choice_service = AdventureChoiceService()

        self.attack_action = AttackAction(
            state_manager=self.state_manager,
            combat_service=self.combat_service,
            resolver=self.resolver,
            runtime_player_service=self.runtime_player_service,
            choice_service=self.choice_service,
            narrate_fn=self._narrate,
            response_fn=self._response,
        )

    def _response(self, event_type: str, text: str, result=None, world=None, choices=None, turn_state=None):
        return {
            "action": event_type,
            "event_type": event_type,
            "text": text,
            "result": result or {},
            "world": world or {},
            "choices": choices or [],
            "turn_state": turn_state or {},
        }

    def _narrate(self, action: str, result: dict, world: dict | None = None):
        llm = LLMService()
        return llm.generate_event_narration({
            "event_type": action,
            "result": result,
            "world": world or {}
        })

    def _advance_turn(self, room_obj, user_id):
        if not room_obj.turn_order:
            room_obj.turn_order = [user_id]

        if user_id not in room_obj.turn_order:
            room_obj.turn_order.append(user_id)

        if room_obj.current_player_id is None:
            room_obj.current_player_id = room_obj.turn_order[0]
            room_obj.current_turn_index = 0
            return room_obj.current_player_id

        current_index = room_obj.turn_order.index(room_obj.current_player_id)
        next_index = (current_index + 1) % len(room_obj.turn_order)
        room_obj.current_player_id = room_obj.turn_order[next_index]
        room_obj.current_turn_index = next_index
        return room_obj.current_player_id

    def _record_history(self, room_obj, user_id, action, result):
        if user_id not in room_obj.player_histories:
            room_obj.player_histories[user_id] = []
        room_obj.player_histories[user_id].append({
            "action": action,
            "result": result,
            "timestamp": len(room_obj.player_histories[user_id]),
        })

    def _turn_state(self, room_obj, user_id):
        return {
            "current_player_id": room_obj.current_player_id,
            "current_turn_index": room_obj.current_turn_index,
            "turn_order": room_obj.turn_order,
            "is_your_turn": room_obj.current_player_id == user_id,
            "history": room_obj.player_histories.get(user_id, []),
        }

    def process(self, parsed_input):
        logger.info(f"[ACTION PROCESS] input={parsed_input}")

        action = parsed_input.get("action")
        world = parsed_input.get("world")

        if parsed_input.get("error") == "unknown_intent_fallback":
            return self._handle_inspect(parsed_input)

        if not action or action == "unknown":
            return self._response(
                "unknown",
                "Invalid action",
                {"error": "invalid_action"}
            )

        room = parsed_input.get("room")
        user_id = parsed_input.get("user_id")
        room_obj = self.state_manager.get_or_create_room(
            self.state_manager.normalize_room_id(room)
        )

        if user_id is not None:
            if user_id not in room_obj.turn_order:
                room_obj.turn_order.append(user_id)
            if room_obj.current_player_id is None:
                room_obj.current_player_id = user_id
                room_obj.current_turn_index = 0
            room_obj.player_histories.setdefault(user_id, [])

        if action == "attack":
            result = self.attack_action.handle(parsed_input, world)

            if user_id is not None:
                self._record_history(room_obj, user_id, action, result.get("result", {}))
                self._advance_turn(room_obj, user_id)
                result["turn_state"] = self._turn_state(room_obj, user_id)

            return result

        if action == "inspect":
            result = self._handle_inspect(parsed_input, world)

            if user_id is not None:
                self._record_history(room_obj, user_id, action, result.get("result", {}))
                self._advance_turn(room_obj, user_id)
                result["turn_state"] = self._turn_state(room_obj, user_id)

            return result

        if action == "move":
            result = self._handle_move(parsed_input, world)

            if user_id is not None:
                self._record_history(room_obj, user_id, action, result.get("result", {}))
                self._advance_turn(room_obj, user_id)
                result["turn_state"] = self._turn_state(room_obj, user_id)

            return result

        if action == "look":
            return self._handle_inspect(parsed_input, world)

        if action == "talk":
            result = NPCService(self.state_manager).talk(
                parsed_input["room"],
                parsed_input["target"]
            )
            return self._response("talk", result.get("text", ""), result)

        return self._response(action, "Unhandled action", {"error": "unhandled_action"})


    # -------------------------
    # INSPECT
    # -------------------------
    def _handle_inspect(self, parsed_input, world=None):
        room = parsed_input.get("room")
        user_id = parsed_input.get("user_id")

        room_key = self.state_manager.normalize_room_id(room)
        room_obj = self.state_manager.get_or_create_room(room_key)

        self.runtime_player_service.get_or_create(room_obj, user_id)
        enemies = list(room_obj.enemies.keys())

        narration = self._narrate("inspect", {
            "room": room_key,
            "enemies": enemies
        }, world)

        choices = self.choice_service.build_choices(
            adventure_id=parsed_input.get("adventure"),
            room_key=room_key,
            event_type="inspect",
            result={"room": room_key, "enemies": enemies},
            world=world,
        )

        return self._response(
            "inspect",
            narration.get("text", "Rozglądasz się po okolicy"),
            {"room": room_key, "enemies": enemies},
            world,
            choices,
        )

    # -------------------------
    # MOVE
    # -------------------------
    def _handle_move(self, parsed_input, world=None):
        room = parsed_input.get("room")
        user_id = parsed_input.get("user_id")
        target = parsed_input.get("target")

        room_key = self.state_manager.normalize_room_id(room)
        room_obj = self.state_manager.get_or_create_room(room_key)

        player = self.runtime_player_service.get_or_create(room_obj, user_id)

        if not player:
            return self._response("move", "Player not found", {"error": "no_player"})

        player.location = target or "unknown"

        narration = self._narrate("move", {
            "location": player.location
        }, world)

        choices = self.choice_service.build_choices(
            adventure_id=parsed_input.get("adventure"),
            room_key=room_key,
            event_type="move",
            result={"location": player.location},
            world=world,
        )

        return self._response(
            "move",
            narration.get("text", f"Przemieszczasz się do: {player.location}"),
            {"location": player.location},
            world,
            choices,
        )