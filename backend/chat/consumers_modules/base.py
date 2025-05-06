# chat/consumers/base.py
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class BaseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.get_room_group_name()

        # Autoryzacja JWT
        token = self.get_token_from_query_string()

        if token:
            try:
                user = await self.authenticate_user(token)
                if user:
                    self.scope["user"] = user
                    await self.accept()
                else:
                    await self.close()
                    return
            except jwt.ExpiredSignatureError:
                await self.close()
                return
        else:
            self.scope["user"] = None
            await self.close()
            return

        await self.on_connect()

    def get_token_from_query_string(self):
        query_string = parse_qs(self.scope["query_string"].decode())
        return query_string.get("token", [None])[0]

    async def authenticate_user(self, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            User = get_user_model()
            user = await User.objects.aget(id=payload["user_id"])
            return user
        except jwt.ExpiredSignatureError:
            await self.send_error_message("Token wygasł")
        except jwt.DecodeError:
            await self.send_error_message("Nieprawidłowy token")
        except User.DoesNotExist:
            await self.send_error_message("Użytkownik nie istnieje")
        return None

    async def send_error_message(self, message):
        await self.send(text_data=json.dumps({
            'message': message,
            'username': 'System'
        }))
        await self.close()

    def get_room_group_name(self):
        return f"{self.__class__.__name__.lower()}_{self.room_name}"

    async def on_connect(self):
        """Dołącz do grupy. Może zostać nadpisana w subclassach."""
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Dołącz do grupy. Może zostać nadpisana w subclassach."""
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        """Przetwarzanie wiadomości. Do nadpisania w subclassach."""
        raise NotImplementedError

    async def send_message(self, message, username):
        """Wysyłanie wiadomości do grupy"""
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )
