from rest_framework import serializers
import logging
from .models import Room
from adventures.serializers import Adventure

logger = logging.getLogger(__name__)

class RoomSerializer(serializers.ModelSerializer):
    adventure = serializers.PrimaryKeyRelatedField(queryset=Adventure.objects.all(), required=False, allow_null=True)
    adventure_title = serializers.CharField(source='adventure.title', read_only=True, allow_null=True)
    
    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ('owner', 'created_at')

    def to_internal_value(self, data):
        logger.info(f"to_internal_value - otrzymane dane: {data}")
        try:
            if 'adventure' in data and data['adventure'] is None:
                data.pop('adventure')
            internal_value = super().to_internal_value(data)
            logger.info(f"to_internal_value - przetworzone dane: {internal_value}")
            return internal_value
        except Exception as e:
            logger.error(f"Błąd w to_internal_value: {str(e)}")
            raise

    def validate(self, data):
        logger.info(f"validate - rozpoczęcie walidacji")
        logger.info(f"validate - otrzymane dane: {data}")
        
        try:
            if 'name' in data:
                logger.info(f"validate - sprawdzanie nazwy: {data['name']}")
                if Room.objects.filter(name=data['name']).exists():
                    logger.error(f"validate - pokój o nazwie {data['name']} już istnieje")
                    raise serializers.ValidationError({"name": "Pokój o tej nazwie już istnieje"})
                logger.info("validate - nazwa jest unikalna")
            
            if 'adventure' in data and data['adventure']:
                logger.info(f"validate - sprawdzanie przygody: {data['adventure']}")
                try:
                    Adventure.objects.get(id=data['adventure'].id)
                    logger.info("validate - przygoda istnieje")
                except Adventure.DoesNotExist:
                    logger.error(f"validate - przygoda o id {data['adventure']} nie istnieje")
                    raise serializers.ValidationError({"adventure": "Wybrana przygoda nie istnieje"})
            
            logger.info("validate - walidacja zakończona pomyślnie")
            return data
        except Exception as e:
            logger.error(f"validate - błąd podczas walidacji: {str(e)}")
            raise