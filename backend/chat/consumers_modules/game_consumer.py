# chat/consumers/game_consumer.py
import json
from .base import BaseConsumer

class GameConsumer(BaseConsumer):
    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            action = text_data_json.get('action', '')
            sender = text_data_json.get('sender', 'Gracz')

            if action == "move":
                message = f"{sender} porusza się."
            elif action == "attack":
                message = f"{sender} atakuje!"
            else:
                message = f"{sender}: {action}"

            await self.send_message(message, sender)
        except Exception as e:
            await self.send_error_message(f"Błąd podczas przetwarzania wiadomości: {e}")
