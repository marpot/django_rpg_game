import pytest
from django.contrib.auth import get_user_model

from game.core.action_processor import ActionProcessor

from game.state.game_state_manager import GameStateManager
from game.state.runtime.models import Player, Enemy

from game.services.combat_service import CombatService
from game.services.dice_service import DiceService


from accounts.models import PlayerCharacter

from world.models import Adventure, Enemy as EnemyORM


pytestmark = pytest.mark.django_db


def test_attack_action():
    state = GameStateManager()
    state.get_or_create_room("testroom")

    User = get_user_model()
    user = User.objects.create_user(username="hero", password="x")

    state.add_player(
        "testroom",
        user.id,
        Player(
            id=user.id,
            name="Hero",
            hp=100,
            max_hp=100,
            attack_bonus=10,
            damage_die=8,
            damage_bonus=2,
            defense=5,
        )
    )

    state.add_enemy(
        "testroom",
        Enemy(
            id="goblin",
            name="goblin",
            hp=10,
            defense=2,
            attack_bonus=1,
            damage_die=6,
            damage_bonus=1,
        )
    )

    PlayerCharacter.objects.create(
        user=user,
        name="Hero",
        health=100,
        max_health=100,
    )

    adventure = Adventure.objects.create(
        title="test",
        creator=user
    )

    EnemyORM.objects.create(
        name="goblin",
        hp=10,
        defense=2,
        attack_bonus=1,
        damage_die=6,
        damage_bonus=1,
        adventure=adventure,
    )

    dice = DiceService(seed=1)
    combat = CombatService(dice)

    processor = ActionProcessor(state_manager=state, combat_service=combat)

    result = processor.process({
        "action": "attack",
        "target": "goblin",
        "room": "testroom",
        "user_id": user.id,
        'adventure': adventure.id
    })

    assert result["action"] == "attack"
    assert "error" not in result
    assert state.get_room("testroom").enemies["goblin"].hp < 10


def test_turn_progresses_and_tracks_player_history():
    state = GameStateManager()
    room = state.get_or_create_room("turnroom")

    User = get_user_model()
    user_one = User.objects.create_user(username="hero1", password="x")
    user_two = User.objects.create_user(username="hero2", password="x")

    room.players[user_one.id] = Player(
        id=user_one.id,
        name="Hero1",
        hp=100,
        max_hp=100,
        attack_bonus=10,
        damage_die=8,
        damage_bonus=2,
        defense=5,
    )
    room.players[user_two.id] = Player(
        id=user_two.id,
        name="Hero2",
        hp=100,
        max_hp=100,
        attack_bonus=10,
        damage_die=8,
        damage_bonus=2,
        defense=5,
    )

    room.turn_order = [user_one.id, user_two.id]
    room.current_player_id = user_one.id
    room.current_turn_index = 0
    room.player_histories = {user_one.id: [], user_two.id: []}

    adventure = Adventure.objects.create(title="turn-test", creator=user_one)

    processor = ActionProcessor(state_manager=state)

    result = processor.process({
        "action": "inspect",
        "room": "turnroom",
        "user_id": user_one.id,
        "adventure": adventure.id,
        "world": {},
    })

    assert result["action"] == "inspect"
    assert room.current_player_id == user_two.id
    assert room.player_histories[user_one.id][-1]["action"] == "inspect"