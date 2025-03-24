from rest_framework import serializers
from django.contrib.auth import get_user_model  							# Używamy get_user_model, aby odwołać się do niestandardowego modelu użytkownika, jeśli jest zdefiniowany
from rest_framework_simplejwt.tokens import RefreshToken  					# Importujemy RefreshToken, który będzie generować tokeny JWT
from .models import PlayerCharacter

User = get_user_model()  # Przypisujemy do zmiennej User model użytkownika

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

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField() 
    password = serializers.CharField(write_only=True)  						# Zdefiniowanie pola hasła jako tylko do zapisu (write_only=True)

    class Meta:
        model = User  														# Określamy, że ten serializer dotyczy modelu User
        fields = ['username', 'email', 'password']  						# Pola, które będą używane w rejestracji

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  					# Nadpisujemy metodę create, aby stworzyć użytkownika
        return user  														# Zwracamy stworzonego użytkownika

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()  									# Pole dla nazwy użytkownika
    password = serializers.CharField()  									# Pole dla hasła

    def validate(self, attrs):
        username = attrs.get('username')  									# Pobieramy dane wejściowe z atrybutów
        password = attrs.get('password')  									# Pobieramy dane wejściowe z atrybutów

        user = User.objects.filter(username=username).first()  				# Szukamy użytkownika w bazie danych po nazwie użytkownika

        if not user or not user.check_password(password):  					# Jeśli użytkownik nie istnieje lub hasło jest niepoprawne, zgłaszamy błąd
            raise serializers.ValidationError("Invalid credentials")  		# Zgłaszamy błąd walidacji, jeśli dane są niepoprawne

        refresh = RefreshToken.for_user(user)  								# Jeśli wszystko jest w porządku (użytkownik istnieje, hasło poprawne), tworzymy tokeny JWT
        return {  															# Zwracamy oba tokeny: refresh i access (token odświeżania i dostępowy)
            'refresh': str(refresh),  										# Zwracamy token odświeżania jako string
            'access': str(refresh.access_token),  	
            'userId': user.id,			                                    # Zwracamy userId			
        }
