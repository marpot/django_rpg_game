
---
```markdown
# Notatki

## Podstawy Django REST Framework (DRF)

1. **Django REST Framework** to narzędzie do budowania API w Django, które pozwala łatwo tworzyć, edytować i zarządzać interfejsami RESTful.

### Serializery (Serializers)

- **Czym są serializery?**
  Serializery w DRF są odpowiedzialne za konwersję danych między formatem Pythonowym (np. modelami Django) a formatem, który może być przesyłany przez API (np. JSON).

- **Rodzaje serializerów**:
  - **`ModelSerializer`**: Używamy go, gdy chcemy łatwo serializować dane z modelu Django.
  - **`Serializer`**: Ogólny serializer, który można stosować do innych przypadków.

### Tworzenie własnych serializerów

#### Rejestracja użytkownika (UserRegisterSerializer)

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

#### Logowanie użytkownika (LoginSerializer)

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

### Uwierzytelnianie za pomocą JWT

- **JWT (JSON Web Tokens)** to popularny sposób uwierzytelniania użytkowników w API.
- **Refresh Token**: Służy do odświeżania tokenów.
- **Access Token**: Krótkoterminowy token, który zapewnia dostęp do chronionych zasobów API.

#### Generowanie tokenów

```python
refresh = RefreshToken.for_user(user)
return {
    'refresh': str(refresh),
    'access': str(refresh.access_token),
}
```

### Błędy walidacji

- **`serializers.ValidationError`**: Używamy tej klasy do zgłaszania błędów walidacji.

```python
if not user or not user.check_password(password):
    raise serializers.ValidationError("Invalid credentials")
```

---

## Jak działają serializery w Django REST Framework?

### Zadanie serializera

Serializery są odpowiedzialne za konwersję danych pomiędzy formatami (np. model Pythonowy → JSON).

### Metoda `validate()`

- Służy do dodatkowej walidacji danych.
- Zgłasza wyjątek `ValidationError` w przypadku niepoprawnych danych.

```python
def validate(self, attrs):
    username = attrs.get('username')
    password = attrs.get('password')

    user = User.objects.filter(username=username).first()

    if not user or not user.check_password(password):
        raise serializers.ValidationError("Invalid credentials")
```

### Metoda `create()`

- Używamy jej do dostosowania sposobu tworzenia obiektów w bazie danych.

```python
def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user
```

---

## Kroki, które wykonaliśmy

1. **Utworzenie aplikacji Django i włączenie DRF**.
2. **Utworzenie modeli i serializerów dla użytkowników**.
3. **Generowanie tokenów JWT**.

---

## Wskazówki i rzeczy do zapamiętania

- **Serializery** w DRF to potężne narzędzie do konwersji danych, walidacji i tworzenia obiektów w bazie danych.
- **`ModelSerializer`**: Używaj go, gdy chcesz połączyć dane z modelem Django.
- **Tokeny JWT**: Przydatne do zarządzania sesjami użytkowników w API.

---

## React - Funkcja strzałkowa vs. Zwykła funkcja

### Funkcja strzałkowa (Arrow Function)

```jsx
const Room = () => {
  return (
    <div>
      <h1>Welcome to the Game Room</h1>
    </div>
  );
};
```

- **Zalety**:
  - Krótsza składnia.
  - Nie tworzy własnego `this`.
  - Częściej stosowana w nowoczesnym React.
  
- **Wady**:
  - Trudniejsza do zrozumienia dla początkujących.

### Zwykła funkcja (Function Declaration)

```jsx
function Room() {
  return (
    <div>
      <h1>Welcome to the Game Room</h1>
    </div>
  );
}
```

- **Zalety**:
  - Łatwiejsza dla początkujących.
  - Możliwość użycia `this`.

- **Wady**:
  - Tworzy własny `this`.
  - Dłuższa składnia.

---

## Notatki z budowy aplikacji RPG w React

### Co to jest React?

React to biblioteka JavaScript do budowania interfejsów użytkownika, stworzona przez Facebook. Dzięki komponentom, React umożliwia tworzenie złożonych aplikacji w sposób modularny.

### Stan (State) w React

- **`useState`**: Funkcja do tworzenia stanu w komponencie funkcyjnym.

```jsx
const [username, setUsername] = useState('');
```

### Routing w React z react-router-dom

Instalacja:

```bash
npm install react-router-dom
```

Przykład:

```jsx
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </Router>
  );
}
```

### Komunikacja z API

Instalacja Axios:

```bash
npm install axios
```

Przykład:

```jsx
import axios from 'axios';

const handleLogin = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/accounts/login/', {
      username: 'user',
      password: 'password'
    });
    localStorage.setItem('access', response.data.access);
  } catch (error) {
    console.error('Błąd logowania', error);
  }
};
```

### Podstawowe błędy w React

- Błąd w zwracaniu JSX: Używaj `return (...)`, nie `return { ... }`.
- Upewnij się, że komponenty są poprawnie zaimportowane i używane.
- Pamiętaj o używaniu funkcji do zmiany stanu (`useState` lub `setState`).

---

## Podsumowanie

- **React** to framework umożliwiający budowanie aplikacji webowych w sposób komponentowy i deklaratywny.
- **Stan (state)** pozwala przechowywać i aktualizować dane.
- **Routing** w React realizujemy za pomocą `react-router-dom`.
- Komponenty są kluczowe dla modularności i utrzymywalności aplikacji w React.

---

Mam nadzieję, że te notatki będą dla Ciebie pomocne! Jeśli masz jakieś pytania lub potrzebujesz dodatkowych wyjaśnień, śmiało pytaj. 😊
```