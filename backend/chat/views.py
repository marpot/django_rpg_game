from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response


from .models import Room
from .serializers import RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RoomDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, room_id):
        try:
            return Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            raise PermissionDenied("The room does not exist.")

    def get(self, request, room_id):
        room = self.get_object(room_id)
        serializer = RoomSerializer(room)
        return Response(serializer.data)
        

