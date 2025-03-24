from rest_framework import serializers
from .models import PlayerCharacter

class PlayerCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerCharacter
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, data):
        if data.get('health', 0) > data.get('max_health', 100):
            raise serializers.ValidationError("Health cannot exceed max_health")
        if data.get('mana', 0) > data.get('max_mana', 50):
            raise serializers.ValidationError("Mana cannot exceed max_mana")
        return data

    def create(self, validated_data):
        # Inicjalizacja pól JSON jeśli nie są podane
        if 'equipment' not in validated_data:
            validated_data['equipment'] = {}
        if 'inventory' not in validated_data:
            validated_data['inventory'] = []
        if 'skills' not in validated_data:
            validated_data['skills'] = []
        if 'status_effects' not in validated_data:
            validated_data['status_effects'] = []
        if 'progress' not in validated_data:
            validated_data['progress'] = {}
        return super().create(validated_data) 