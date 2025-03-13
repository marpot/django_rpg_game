from django.shortcuts import render
from rest_framework import viewsets
from .models import PlayerCharacter, GameSession, GameEvent
from .serializers import PlayerCharacterSerializer, GameSessionSerializer, GameEventSerializer

class PlayerCharacterViewSet(viewsets.ModelViewSet):
    queryset = PlayerCharacter.objects.all()
    serializer_class = PlayerCharacterSerializer

class GameSessionViewSet(viewsets.ModelViewSet):
    queryset = GameSession.objects.all()
    serializer_class = GameSessionSerializer

class GameEventViewSet(viewsets.ModelViewSet):
    queryset = GameEvent.objects.all()
    serializer_class = GameEventSerializer