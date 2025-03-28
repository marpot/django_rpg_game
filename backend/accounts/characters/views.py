from rest_framework import viewsets
from .models import PlayerCharacter
from .serializers import PlayerCharacterSerializer

class PlayerCharacterViewSet(viewsets.ModelViewSet):
    queryset = PlayerCharacter.objects.all()
    serializer_class = PlayerCharacterSerializer

    def get_queryset(self):
        return PlayerCharacter.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 