from rest_framework import serializers
from django.contrib.auth import get_user_model  							# Używamy get_user_model, aby odwołać się do niestandardowego modelu użytkownika, jeśli jest zdefiniowany
from rest_framework_simplejwt.tokens import RefreshToken  					# Importujemy RefreshToken, który będzie generować tokeny JWT

User = get_user_model()  # Przypisujemy do zmiennej User model użytkownika

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  						# Zdefiniowanie pola hasła jako tylko do zapisu (write_only=True)

    class Meta:
        model = User  														# Określamy, że ten serializer dotyczy modelu User
        fields = ['username', 'email', 'password']  						# Pola, które będą używane w rejestracji

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  					# Nadpisujemy metodę create, aby stworzyć użytkownika
        return user  														# Zwracamy stworzonego użytkownika

class LoginSerializer(serializers.Serializer):
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
            'access': str(refresh.access_token),  							# Zwracamy token dostępu (access token) jako string
        }
