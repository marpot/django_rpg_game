from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import PlayerCharacter

User = get_user_model()


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
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        # Krok A: Zawsze pokazujemy co dostajemy z frontendu
        print("=== [LOGIN DEBUG] START ===", flush=True)
        print(f"DEBUG LOGIN - Otrzymane dane: {attrs}", flush=True)

        # Krok B: Wyciągamy pola
        email = attrs.get('email')
        username = attrs.get('username')
        password = attrs.get('password')

        # Debug - zobaczymy co dokładnie dostajemy
        print(f"DEBUG LOGIN - Otrzymane dane: {attrs}", flush=True)

        # Krok C: Sprawdzamy czy jest hasło
        if not password:
            print("DEBUG LOGIN - ERROR: No password provided", flush=True)
            raise serializers.ValidationError({"detail": "Hasło jest wymagane."})

        # Krok D: Sprawdzamy czy jest chociaż jeden login (email lub username)
        if not email and not username:
            print("DEBUG LOGIN - ERROR: Neither email nor username provided", flush=True)
            raise serializers.ValidationError({"detail": "Email lub username jest wymagany."})

        # Krok E: Logowanie przez email (priorytet)
        if email:
            print(f"DEBUG LOGIN - Próba logowania przez EMAIL: {email}", flush=True)
            try:
                user = User.objects.get(email=email)
                print(f"DEBUG LOGIN - Znaleziono użytkownika po emailu: {user.username} (id={user.id})", flush=True)
            except User.DoesNotExist:
                print("DEBUG LOGIN - Nie znaleziono użytkownika o podanym emailu", flush=True)
                raise serializers.ValidationError({"detail": "Nieprawidłowe dane logowania."})
        # Krok F: Logowanie przez username (jeśli nie było emaila)
        else:
            print(f"DEBUG LOGIN - Próba logowania przez USERNAME: {username}", flush=True)
            user = User.objects.filter(username=username).first()
            if not user:
                print("DEBUG LOGIN - Nie znaleziono użytkownika o podanym username", flush=True)
                raise serializers.ValidationError({"detail": "Nieprawidłowe dane logowania."})

        if not user.check_password(password):
            print("DEBUG LOGIN - Hasło niepoprawne", flush=True)
            raise serializers.ValidationError({"detail": "Nieprawidłowe dane logowania."})

        print(f"DEBUG LOGIN - Logowanie udane dla użytkownika: {user.username}", flush=True)
        print("=== [LOGIN DEBUG] END ===\n", flush=True)

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'userId': user.id,
            'username': user.username,
        }