from rest_framework import serializers
from .models import Room
from adventures.serializers import Adventure


class RoomSerializer(serializers.ModelSerializer):
    adventure = serializers.PrimaryKeyRelatedField(queryset=Adventure.objects.all(), required=False)
    adventure_title = serializers.CharField(source='adventure.title', read_only=True)
    class Meta:
        model = Room
        fields = '__all__'