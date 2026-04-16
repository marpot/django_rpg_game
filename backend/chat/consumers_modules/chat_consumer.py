# chat/consumers/chat_consumer.py
import json
from .base import BaseConsumer

class ChatConsumer(BaseConsumer):
    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get('message', '').strip()

            if not message:
                return

            user = self.scope.get('user', None)
            username = user.username if user and user.is_authenticated else 'Anonim'

            await self.send_message(message, username)
        except json.JSONDecodeError:
            await self.send_error_message("Niepoprawny format wiadomości")
