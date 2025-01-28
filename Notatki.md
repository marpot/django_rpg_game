Jasne, poniżej przedstawiam te same notatki, ale z przykładami kodu, które masz w swojej aplikacji. Będziesz mógł zobaczyć jak poszczególne części wyglądają w kodzie.

---

### **Podstawy Django REST Framework (DRF)**

1. **Django REST Framework** to narzędzie do budowania API w Django, które pozwala łatwo tworzyć, edytować i zarządzać interfejsami RESTful. 

2. **Serializery (Serializers)**:
   - **Czym są serializery?**: Serializery w DRF są odpowiedzialne za konwersję danych między formatem Pythonowym (np. modelami Django) a formatem, który może być przesyłany przez API (np. JSON).
   - **Rodzaje serializerów**:
     - **`ModelSerializer`**: Używa się go, gdy chcemy łatwo serializować dane z modelu Django. Automatycznie generuje pola i logikę walidacji na podstawie modelu.
     - **`Serializer`**: Ogólny serializer, który można stosować do innych przypadków, gdzie nie korzystamy bezpośrednio z modelu Django.

3. **Tworzenie własnych serializerów**:
   - **Rejestracja użytkownika (UserRegisterSerializer)**:
     - Używamy **`ModelSerializer`** do serializacji danych użytkownika (username, email, password).
     - **write_only=True** w przypadku pola hasła oznacza, że dane to będą tylko zapisywane, ale nie zwracane w odpowiedzi API.
     - Nadpisanie metody `create()` pozwala na tworzenie użytkownika z wykorzystaniem metody **`create_user`**, która automatycznie haszuje hasło.

   **Przykład kodu:**
   ```python
   class UserRegisterSerializer(serializers.ModelSerializer):
       password = serializers.CharField(write_only=True)

       class Meta:
           model = User
           fields = ['username', 'email', 'password']

       def create(self, validated_data):
           user = User.objects.create_user(**validated_data)
           return user
   ```

   - **Logowanie użytkownika (LoginSerializer)**:
     - Używamy **`Serializer`** do serializacji danych wejściowych (username, password).
     - W metodzie **`validate`** sprawdzamy poprawność loginu i hasła:
       - Pobieramy użytkownika na podstawie nazwy użytkownika.
       - Sprawdzamy, czy hasło jest poprawne (przy pomocy `check_password`).
     - Jeśli dane są poprawne, tworzymy tokeny JWT (JSON Web Tokens), które pozwalają na uwierzytelnienie w API.

   **Przykład kodu:**
   ```python
   class LoginSerializer(serializers.Serializer):
       username = serializers.CharField()
       password = serializers.CharField()

       def validate(self, attrs):
           username = attrs.get('username')
           password = attrs.get('password')

           user = User.objects.filter(username=username).first()

           if not user or not user.check_password(password):
               raise serializers.ValidationError("Invalid credentials")

           refresh = RefreshToken.for_user(user)
           return {
               'refresh': str(refresh),
               'access': str(refresh.access_token),
           }
   ```

4. **Uwierzytelnianie za pomocą JWT**:
   - **JWT** to popularny sposób uwierzytelniania użytkowników w API.
   - **Refresh Token**: Używany do odświeżania tokenów, co umożliwia utrzymanie sesji użytkownika bez konieczności ciągłego logowania.
   - **Access Token**: Krótkoterminowy token, który zapewnia dostęp do chronionych zasobów API.

   **Biblioteka `rest_framework_simplejwt`**:
   - Używamy jej do generowania i walidacji tokenów JWT.
   - **`RefreshToken.for_user(user)`**: Tworzy token odświeżania dla danego użytkownika.
   - W metodzie logowania zwracamy oba tokeny: refresh i access.

   **Przykład kodu (generowanie tokenów):**
   ```python
   refresh = RefreshToken.for_user(user)
   return {
       'refresh': str(refresh),
       'access': str(refresh.access_token),
   }
   ```

5. **Błędy walidacji**:
   - **`serializers.ValidationError`**: Służy do zgłaszania błędów walidacji w przypadku niepoprawnych danych (np. błędne dane logowania).

   **Przykład kodu (błąd walidacji):**
   ```python
   if not user or not user.check_password(password):
       raise serializers.ValidationError("Invalid credentials")
   ```

---

### **Jak działają serializery w Django REST Framework?**

1. **Zadanie serializera**: Serializery są odpowiedzialne za konwersję danych pomiędzy formatami (np. model Pythonowy → JSON).
   
2. **Metoda `validate()`**:
   - Jest to specjalna metoda w serializerze, która umożliwia wykonanie dodatkowej logiki walidacji.
   - W przypadku logowania użytkownika walidujemy poprawność nazwy użytkownika i hasła.
   - Zgłaszamy wyjątek `ValidationError`, jeśli dane wejściowe są niepoprawne.

   **Przykład kodu:**
   ```python
   def validate(self, attrs):
       username = attrs.get('username')
       password = attrs.get('password')

       user = User.objects.filter(username=username).first()

       if not user or not user.check_password(password):
           raise serializers.ValidationError("Invalid credentials")
   ```

3. **Metoda `create()`**:
   - Jeśli używamy **`ModelSerializer`**, możemy nadpisać metodę `create()`, aby dostosować sposób tworzenia obiektów w bazie danych (np. haszowanie hasła podczas tworzenia użytkownika).
   
   **Przykład kodu:**
   ```python
   def create(self, validated_data):
       user = User.objects.create_user(**validated_data)
       return user
   ```

4. **Serializowanie danych użytkownika**:
   - Tworzymy serializer dla rejestracji użytkownika, który zajmuje się konwersją danych z formularza na obiekt użytkownika.
   - Z kolei w przypadku logowania serializujemy dane wejściowe, walidujemy je, a następnie generujemy tokeny JWT, które są zwracane w odpowiedzi.

   **Przykład kodu (serializowanie i walidacja danych):**
   ```python
   class UserRegisterSerializer(serializers.ModelSerializer):
       password = serializers.CharField(write_only=True)

       class Meta:
           model = User
           fields = ['username', 'email', 'password']

       def create(self, validated_data):
           user = User.objects.create_user(**validated_data)
           return user
   ```

   ```python
   class LoginSerializer(serializers.Serializer):
       username = serializers.CharField()
       password = serializers.CharField()

       def validate(self, attrs):
           username = attrs.get('username')
           password = attrs.get('password')

           user = User.objects.filter(username=username).first()

           if not user or not user.check_password(password):
               raise serializers.ValidationError("Invalid credentials")

           refresh = RefreshToken.for_user(user)
           return {
               'refresh': str(refresh),
               'access': str(refresh.access_token),
           }
   ```

---

### **Kroki, które wykonaliśmy**

1. **Utworzenie aplikacji Django i włączenie DRF**:
   - Zainstalowaliśmy Django REST Framework oraz rest_framework_simplejwt.
   - Skonfigurowaliśmy nasze aplikacje w `INSTALLED_APPS`.

2. **Utworzenie modeli i serializerów dla użytkowników**:
   - Stworzyliśmy **`UserRegisterSerializer`** i **`LoginSerializer`**, które obsługują rejestrację i logowanie użytkowników.

3. **Generowanie tokenów JWT**:
   - Po walidacji danych użytkownika generujemy tokeny JWT (access token i refresh token) dla bezpiecznego uwierzytelniania użytkowników w naszym API.

---

### **Wskazówki i rzeczy do zapamiętania**

- **Serializery** w DRF to potężne narzędzie do konwersji danych, walidacji i tworzenia obiektów w bazie danych.
- **`ModelSerializer`**: Zawsze używaj, gdy chcesz połączyć dane z modelem Django, to upraszcza kod.
- **Tokeny JWT**: Bardzo przydatne do zarządzania sesjami użytkowników w API, zwłaszcza w aplikacjach, które muszą działać bez konieczności przechowywania sesji na serwerze.

---

Teraz masz pełne notatki z kodem, które będziesz mógł wykorzystać w przyszłości. Jeśli masz jakiekolwiek pytania, śmiało pytaj!