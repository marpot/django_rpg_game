import logging
from typing import Any, Dict, List, Optional

from world.models import Choice, Location

logger = logging.getLogger(__name__)


class AdventureChoiceService:
    """Buduje dynamiczne opcje akcji na podstawie przygody i jej lokalizacji."""

    def build_choices(
        self,
        adventure_id: Optional[int] = None,
        room_key: Optional[str] = None,
        event_type: Optional[str] = None,
        result: Optional[Dict[str, Any]] = None,
        world: Optional[Dict[str, Any]] = None,
        limit: int = 4,
    ) -> List[Dict[str, Any]]:
        if adventure_id:
            try:
                locations = list(
                    Location.objects.filter(adventure_id=adventure_id)
                    .prefetch_related("choices")
                )

                choices: List[Dict[str, Any]] = []
                for location in locations:
                    for choice in location.choices.all():
                        choices.append(self._serialize_choice(choice))
                        if len(choices) >= limit:
                            return choices

                if choices:
                    return choices
            except Exception as exc:
                logger.warning(f"[CHOICES] could not load adventure choices: {exc}")

        return self._fallback_choices(adventure_id, room_key, event_type)

    def _serialize_choice(self, choice: Choice) -> Dict[str, Any]:
        title = (choice.title or "Dalej").strip()
        description = (choice.description or "Kontynuuj przygodę").strip()
        message = self._message_from_title(title)
        action = self._infer_action(title)

        return {
            "id": f"choice-{choice.id}",
            "label": title,
            "title": title,
            "description": description,
            "message": message,
            "action": action,
            "target": choice.next_location.title if choice.next_location else None,
        }

    def _message_from_title(self, title: str) -> str:
        text = title.strip().lower()
        if any(token in text for token in ["atak", "walcz", "bój"]):
            return title
        if any(token in text for token in ["rozmawiaj", "mów", "porozmawiaj"]):
            return title
        if any(token in text for token in ["sprawdź", "sprawdz", "zbadaj", "rozejrzyj"]):
            return title
        if any(token in text for token in ["wejdź", "wejdz", "idź", "idz", "pójdź", "pójdz"]):
            return title
        return f"{title}".strip()

    def _infer_action(self, title: str) -> str:
        text = title.lower()
        if any(token in text for token in ["atak", "walcz", "bój"]):
            return "attack"
        if any(token in text for token in ["rozmawiaj", "mów", "porozmawiaj"]):
            return "talk"
        if any(token in text for token in ["sprawdź", "sprawdz", "zbadaj", "rozejrzyj"]):
            return "inspect"
        return "move"

    def _fallback_choices(
        self,
        adventure_id: Optional[int],
        room_key: Optional[str],
        event_type: Optional[str],
    ) -> List[Dict[str, Any]]:
        return [
            {
                "id": "inspect",
                "label": "Rozejrzyj się",
                "title": "Rozejrzyj się",
                "description": "Sprawdź otoczenie i ślady przygody.",
                "message": "sprawdź otoczenie",
                "action": "inspect",
                "target": None,
            },
            {
                "id": "move",
                "label": "Idź dalej",
                "title": "Idź dalej",
                "description": "Przejdź do kolejnego miejsca w przygodzie.",
                "message": "idź dalej",
                "action": "move",
                "target": None,
            },
        ]
