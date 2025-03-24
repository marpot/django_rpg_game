from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
import logging

User = get_user_model()
logger = logging.getLogger(__name__)

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        logger.info(f"Próba logowania użytkownika: {username}")
        
        try:
            user = User.objects.get(username=username)
            logger.info(f"Znaleziono użytkownika: {username}")
            
            if not user.check_password(password):
                logger.error(f"Nieprawidłowe hasło dla użytkownika: {username}")
                raise serializers.ValidationError("No active account found with the given credentials")
            
            logger.info(f"Hasło poprawne dla użytkownika: {username}")
            
            refresh = RefreshToken.for_user(user)
            logger.info(f"Wygenerowano tokeny dla użytkownika: {username}")
            
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'userId': user.id,
                'username': user.username
            }
        except User.DoesNotExist:
            logger.error(f"Nie znaleziono użytkownika: {username}")
            raise serializers.ValidationError("No active account found with the given credentials") 