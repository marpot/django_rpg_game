from django.urls import re_path
from chat.consumers import ChatConsumer, GameConsumer

websocket_urlpatterns = [
	re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
	re_path(r'ws/game/(?P<room_name>\w+)/$', GameConsumer.as_asgi()),
]