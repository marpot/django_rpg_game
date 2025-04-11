# Gra RPG

## Opis projektu

Jest to gra RPG, w której gracze mogą się logować, rejestrować, tworzyć pokoje i wchodzić w interakcje z fabułą. Gracze podejmują decyzje, które wpływają na rozwój fabuły. Gra jest zaprojektowana jako dynamiczna i interaktywna, oferująca kreatora scenariuszy dla bogatego opowiadania historii i rozgrywki.

## Plan tworzenia gry RPG z kreatorem scenariuszy

### DevOps**
   Priorytety na teraz: działający docker

### **Faza 1: Budowanie fundamentów**

1. **Backend: Django REST Framework**
   - **Autentykacja i zarządzanie użytkownikami** ✅ (Zakończono: 24.03.2024)
     - Rejestracja i logowanie użytkowników z autentykacją JWT
     - Profile graczy (podstawowa implementacja)
     - Implementacja w: `accounts/users/`, `accounts/views.py`, `accounts/serializers.py`
     - Poprawiono obsługę błędów w logowaniu i rejestracji
     - Zaktualizowano testy jednostkowe dla endpointów autentykacji
   - **Modele bazy danych** ✅ (Zakończono: 24.03.2024)
     - **User**: Dane gracza ✅ (zaimplementowane w `accounts/models.py`)
     - **Room**: Pokój gry (scenariusz, status, gracze) ✅ (zaimplementowane w `game/models.py`)
     - **PlayerCharacter**: Postać gracza (podstawowy model) ✅ (zaimplementowane w `accounts/characters/`)
     - **GameEvent**: Historia zdarzeń w grze ✅ (zaimplementowane w `game/models.py`)
     - **Adventure**: Scenariusze przygód ✅ (zaimplementowane w `adventures/models.py`)
     - **Location**: Lokacje w grze ✅ (zaimplementowane w `adventures/locations/`)
     - **Choice**: Wybory w grze ✅ (zaimplementowane w `adventures/models.py`)
      
   - **API** ✅ (Zakończono: 24.03.2024)
     - Rejestracja i logowanie (zaimplementowane w `accounts/views.py`)
     - Tworzenie i dołączanie do pokoi (zaimplementowane w `game/views.py`)
     - Zarządzanie postaciami graczy (zaimplementowane w `accounts/characters/`)
     - Utworzony kreator przygód z możliwością tworzenia przygód, wyborów i lokacji z poziomu panelu administratora

   - **Testowanie automatyczne Backend** ✅ (Zakończono: 24.03.2024)
     - Testowanie punktów końcowych, autentykacji i walidacji danych
     - Implementacja w katalogach `*/tests/`
     - Poprawiono testy dla endpointów logowania i rejestracji
     - Dodano testy dla obsługi błędów
         
         # **Aplikacja Users**
         - Testowanie modeli w aplikacji users (zaimplementowane w `accounts/tests/`)
         - Testowanie serializatorów w aplikacji users (zaimplementowane w `accounts/tests/`)
         - Dodano testy dla CustomUser model
         - Poprawiono testy dla endpointów autentykacji
            
         # **Aplikacja Adventures**
         - Testowanie modeli w aplikacji adventures
         - Testowanie serializatorów w aplikacji adventures

2. **Frontend: TypeScript**
   - **UI logowania i rejestracji** ✅ (Zakończono: 24.03.2024)
     - Stylizowany panel logowania
     - Wyświetlanie listy pokoi gry
     - Tworzenie pokoi
     - Profil gracza (podstawowa implementacja)
   - **UI gry** 🟨 (W trakcie)
     - Interfejs rozgrywki:
       - Wyświetlanie historii wydarzeń 🟨 (częściowo zaimplementowane w `frontend/src/components/`)
       - Wybory gracza i interakcje ❌ (brak implementacji)

3. **Kreator scenariusza** 🟨 (W trakcie)
   - **Stworzenie możliwości tworzenia scenariuszy z poziomu panelu administratora** ✅ (zaimplementowane w `adventures/admin.py`)
   - **Predefiniowane scenariusze fabularne** 🟨 (częściowo zaimplementowane w `adventures/quests/`)
     - Tworzenie wielu gałęzi fabuły
   - **System zasad interakcji** 🟨 (częściowo zaimplementowane w `adventures/models.py`)
     - Określenie jak wybory graczy wpływają na fabułę
   - **Postęp fabuły** ❌ (brak implementacji)
     - Generowanie wyników na podstawie decyzji graczy

4. **Komunikacja w czasie rzeczywistym** 🟨 (W trakcie)
   - WebSockets (Django Channels):
     - Obsługa wymiany danych w czasie rzeczywistym między graczami ✅ (zaimplementowane w `chat/consumers.py`)
     - Synchronizacja działań graczy 🟨 (częściowo zaimplementowane w `chat/views.py`)

### **Faza 2: Rozszerzenie mechaniki rozgrywki** 🟨 (W trakcie)

1. **Współpraca graczy i interakcja** 🟨 (W trakcie)
   - Wspólne zadania (częściowo zaimplementowane w `game/core/`)
   - Handel przedmiotami i wzajemne wsparcie w walce (brak implementacji)

2. **System walki** ❌ (Nie rozpoczęto)
   - **Mechanika turowa** (brak implementacji)
     - Gracze wybierają akcje (atak, obrona, użycie umiejętności)
     - Wyniki określane przez zasady systemu
   - **Statusy i efekty specjalne** (brak implementacji)
     - "Zatruty", "Zamrożony", "Wzmocniony"
   - **Siatka taktyczna (opcjonalnie)** (brak implementacji)
     - Możliwość poruszania się po siatce w czasie walki

3. **Eksploracja i mapa świata** 🟨 (W trakcie)
   - Mapa z dynamicznie generowanymi lokacjami (częściowo zaimplementowane w `adventures/locations/`)
   - Eksploracja przez graczy:
     - Wchodzenie do różnych lokacji (zaimplementowane w `adventures/views.py`)
     - Odkrywanie skarbów i sekretów (brak implementacji)

4. **Unikalne postacie graczy** ❌ (Nie rozpoczęto)
   - Zaawansowany kreator postaci:
     - Wybór rasy, klasy, umiejętności (zaimplementowane w `accounts/characters/`)
   - Rozwój postaci:
     - Zbieranie punktów doświadczenia i rozwój umiejętności (`game/skills/`)
     - Zarządzanie ekwipunkiem i przedmiotami (częściowo zaimplementowane w `game/inventory/`)

### **Faza 3: Ulepszanie doświadczeń graczy** ❌ (Nie rozpoczęto)

1. **System moralności i reputacji** (brak implementacji)
   - Decyzje graczy wpływają na reputację i relacje z NPC
   - Fabuła zmienia się dynamicznie na podstawie wyborów

2. **Wielowątkowe narracje** (brak implementacji)
   - Wielowarstwowe misje i wątki poboczne
   - Długoterminowy postęp fabularny

3. **System osiągnięć** (brak implementacji)
   - Nagrody za specjalne osiągnięcia

4. **Zaawansowana interakcja z fabułą** (brak implementacji)
   - NPC pamiętają działania graczy
   - Fabuła rozwija się na podstawie przeszłych decyzji

### **Faza 4: Multimedia i zanurzenie w grze** ❌ (Nie rozpoczęto)

1. **Efekty dźwiękowe i muzyka** (brak implementacji)
   - Dynamiczna muzyka zależna od lokalizacji i wydarzeń
   - Efekty dźwiękowe dla działań

2. **Ilustracje i grafika** (brak implementacji)
   - Wizualne reprezentacje lokacji, NPC i wydarzeń
   - Personalizowane awatary dla postaci graczy

### **Faza 5: Funkcje społecznościowe** 🟨 (W trakcie)

1. **Czat głosowy i tekstowy**
   - Wbudowany system czatu dla komunikacji między graczami ✅ (tylko tekstowy, zaimplementowane w `chat/`)
2. **Rankingi i rywalizacja** ❌ (brak implementacji)
   - Punkty za ukończone scenariusze
   - Porównywanie wyników drużyn na tablicach wyników

3. **Hosting i skalowanie** ❌ (brak implementacji)
   - Hosting backendu i frontendu w chmurze
   - Skalowanie serwerów do obsługi dużej liczby graczy

### **Faza 6: Testowanie i optymalizacja** 🟨 (W trakcie)

1. **Testowanie**
   - Testy automatyczne funkcjonalności ✅ (zaimplementowane w katalogach `*/tests/`)
   - Testowanie interakcji użytkowników 🟨 (częściowo zaimplementowane)
   - Testowanie wydajności pod kątem skalowalności ❌ (brak implementacji)

2. **Optymalizacja** 🟨 (W trakcie)
   - Udoskonalenie kodu frontendowego i backendowego
   - Dostosowanie algorytmów do interakcji z dużą liczbą użytkowników

### **Status projektu (24.03.2024)**
- ✅ Zakończone: 30%
- 🟨 W trakcie: 35%
- ❌ Nie rozpoczęte: 35%

### **Następne priorytety**
1. Dokończenie podstawowej mechaniki rozgrywki (implementacja w `game/core/`)
2. Implementacja systemu walki (nowy moduł w `game/combat/`)
3. Rozbudowa kreatora scenariuszy (rozszerzenie w `adventures/`)
4. Implementacja systemu osiągnięć (nowy moduł)
5. Optymalizacja wydajności aplikacji (refaktoryzacja istniejącego kodu)
6. Rozbudowa systemu testów dla nowych funkcjonalności
7. Implementacja systemu czatu głosowego

---

