from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import GameSessionViewSet, GameEventViewSet

router = SimpleRouter()
router.register(r'sessions', GameSessionViewSet)
router.register(r'events', GameEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('events/history/<int:room_id>/', GameEventViewSet.as_view({'get': 'history'}), name='event_history'),
]