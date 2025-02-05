import json
import jwt
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        User = get_user_model()
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        print(f"🔗 Próba połączenia: {self.channel_name} do pokoju {self.room_name}")

        query_string = parse_qs(self.scope["query_string"].decode())
        token = query_string.get("token", [None])[0]

        if token:
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                user = await User.objects.aget(id=payload["user_id"])
                self.scope["user"] = user
                print(f"✅ Uwierzytelniono użytkownika: {user.username}")
            except jwt.ExpiredSignatureError:
                print("❌ Token wygasł")
                await self.close()
                return
            except jwt.DecodeError:
                print("❌ Nieprawidłowy token")
                await self.close()
                return
            except User.DoesNotExist:
                print("❌ Użytkownik nie istnieje")
                await self.close()
                return
        else:
            print("⚠️ Brak tokena – użytkownik anonimowy")
            self.scope["user"] = None

        try:
            if not hasattr(self, "joined"):  # Zapobiega ponownemu dołączaniu
                await self.channel_layer.group_add(self.room_group_name, self.channel_name)
                self.joined = True
            await self.accept()
            print(f"✅ WebSocket połączony ({self.channel_name}) do pokoju {self.room_name}")
        except Exception as e:
            print(f"❌ Błąd przy akceptacji połączenia: {e}")
            await self.close()

    async def disconnect(self, close_code):
        print(f"🔌 Rozłączanie: {self.channel_name} z pokoju {self.room_name}, kod: {close_code}")
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        try:
            print(f"📥 Otrzymana wiadomość surowa: {text_data}")

            text_data_json = json.loads(text_data)
            message = text_data_json.get('message', '').strip()

            if not message:
                print("⚠️ Otrzymano pustą wiadomość, pomijam.")
                return

            user = self.scope.get('user', None)
            username = user.username if user and user.is_authenticated else 'Anonim'

            print(f"📌 Otrzymana wiadomość: {message}, od: {username}")

            message_id = text_data_json.get('message_id', None)
            if message_id and hasattr(self, 'sent_messages') and message_id in self.sent_messages:
                print("⚠️ Pominięto dublującą się wiadomość.")
                return

            if not hasattr(self, 'sent_messages'):
                self.sent_messages = set()

            self.sent_messages.add(message_id)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                    'message_id': message_id,
                }
            )
        except json.JSONDecodeError:
            print("❌ Błąd: Otrzymano niepoprawny JSON")
            await self.send(text_data=json.dumps({
                'message': "❌ Niepoprawny format wiadomości",
                'username': 'System'
            }))
        except Exception as e:
            print(f"❌ Błąd w receive: {e}")
            await self.send(text_data=json.dumps({
                'message': "❌ Błąd podczas przetwarzania wiadomości",
                'username': 'System'
            }))

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        message_id = event.get('message_id', None)

        print(f"📤 Wysyłanie wiadomości: {message} od {username}, id: {message_id}")

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'message_id': message_id,
        }))


class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'game_{self.room_name}'

        print(f"🎮 Próba połączenia z pokojem gry: {self.room_name}")

        try:
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
            print(f"✅ WebSocket połączony z pokojem gry: {self.room_name}")

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'game_message',
                    'message': "Gracz dołączył do gry!",
                    'sender': 'system'
                }
            )
        except Exception as e:
            print(f"❌ Błąd podczas akceptacji połączenia: {e}")
            await self.close()

    async def disconnect(self, close_code):
        print(f"🔌 Rozłączanie z pokojem gry: {self.room_name}, kod: {close_code}")
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

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

            print(f"🎮 Otrzymano akcję: {message}")

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'game_message',
                    'message': message,
                    'sender': sender
                }
            )
        except Exception as e:
            print(f"❌ Błąd podczas przetwarzania wiadomości: {e}")
            await self.close()

    async def game_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender']
        }))
