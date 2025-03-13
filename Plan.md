
---

### **Polska wersja:**

# Gra RPG

## Opis projektu

Jest to gra RPG, w której gracze mogą się logować, rejestrować, tworzyć pokoje i wchodzić w interakcje z fabułą. Gracze podejmują decyzje, które wpływają na rozwój fabuły. Gra jest zaprojektowana jako dynamiczna i interaktywna, oferująca kreatora scenariuszy dla bogatego opowiadania historii i rozgrywki.

## Plan tworzenia gry RPG z kreatorem scenariuszy

### **Faza 1: Budowanie fundamentów**

TERAZ 3.03.2025: zrobić

1. **Backend: Django REST Framework**
   - **Autentykacja i zarządzanie użytkownikami**:
     - Rejestracja i logowanie użytkowników z autentykacją JWT. **(ZROBIONE)**
     - Profile graczy. **(ZROBIONE)**
   - **Modele bazy danych**:
     - **User**: Dane gracza. **(ZROBIONE)**
     **Room**: Pokój gry (scenariusz, status, gracze). **(Nie zrobione)**
     - **PlayerCharacter**: Postać gracza (statystyki, ekwipunek). *(Aktualnie tylko poziom w modelach)* **(W TRAKCIE)**
     - **GameEvent**: Historia zdarzeń w grze. **(Nie zrobione)**
      
   - **API**:
     - Rejestracja i logowanie. **(ZROBIONE)**
     - Tworzenie i dołączanie do pokoi. **(ZROBIONE)**
      - Utworzony kreator przygód z możliwością tworzenia przygód, wyborów i lokacji z poziomu panelu administratora **(ZROBIONE)**

   - **Testowanie automatyczne Backend**:
     - Testowanie punktów końcowych, autentykacji i walidacji danych. **(ZROBIONE)**
         
      # **Aplikacja Users**
      - Testowanie modeli w aplikaji users. **(ZROBIONE)**
      - Testowanie serializatorów w aplikacji users **(ZROBIONE)**
      
      # **Aplikacja Adventures**
      - Testowanie modeli w aplikacji adventures **(ZROBIONE)**
      - Testowanie serializatorów w aplikacji adventures **(ZROBIONE)**
      

2. **Frontend: JavaScript**
   - **UI logowania i rejestracji**:
     - Stylizowany panel logowania. **(ZROBIONE)**
     - Wyświetlanie listy pokoi gry. **(ZROBIONE)**
     - Tworzenie pokoi. **(NIE ZACZĘTO)**
   - **UI gry**:
     - Interfejs rozgrywki:
       - Wyświetlanie historii wydarzeń. **(NIE ZACZĘTO)**
       - Wybory gracza i interakcje. **(NIE ZACZĘTO)**

3. **Kreator scenariusza**:
   - **Stworzenie możliwości tworzenia scenariuszy z poziomu panelu administratora - bardzo podstawowe (ZROBIONE!)** :
   - **Predefiniowane scenariusze fabularne**:
     - Tworzenie wielu gałęzi fabuły. **(NIE ZACZĘTO)**
   - **System zasad interakcji**:
     - Określenie jak wybory graczy wpływają na fabułę. **(NIE ZACZĘTO)**
   - **Postęp fabuły**:
     - Generowanie wyników na podstawie decyzji graczy. **(NIE ZACZĘTO)**


4. **Komunikacja w czasie rzeczywistym**:
   - WebSockets (Django Channels):
     - Obsługa wymiany danych w czasie rzeczywistym między graczami i systemem. **(ZROBIONE między graczami)**
     - Synchronizacja działań graczy. **(NIE ZACZĘTO)**

---

### **Faza 2: Rozszerzenie mechaniki rozgrywki**

1. **Współpraca graczy i interakcja**:
   - Wspólne zadania i decyzje. **(NIE ZACZĘTO)**
   - Handel przedmiotami i wzajemne wsparcie w walce. **(NIE ZACZĘTO)**

2. **System walki**:
   - **Mechanika turowa**:
     - Gracze wybierają akcje (atak, obrona, użycie umiejętności). **(NIE ZACZĘTO)**
     - Wyniki określane przez zasady systemu. **NIE ZACZĘTO**
   - **Statusy i efekty specjalne**:
     - "Zatruty", "Zamrożony", "Wzmocniony". **(NIE ZACZĘTO)**
   - **Siatka taktyczna (opcjonalnie)**:
     - Możliwość poruszania się po siatce w czasie walki. **(NIE ZACZĘTO)**

3. **Eksploracja i mapa świata**:
   - Mapa z dynamicznie generowanymi lokacjami. **(NIE ZACZĘTO)**
   - Eksploracja przez graczy:
     - Wchodzenie do różnych lokacji. **(NIE ZACZĘTO)**
     - Odkrywanie skarbów i sekretów. **(NIE ZACZĘTO)**

4. **Unikalne postacie graczy**:
   - Zaawansowany kreator postaci:
     - Wybór rasy, klasy, umiejętności. **(NIE ZACZĘTO)**
   - Rozwój postaci:
     - Zbieranie punktów doświadczenia i rozwój umiejętności. **(NIE ZACZĘTO)**
     - Zarządzanie ekwipunkiem i przedmiotami. **(NIE ZACZĘTO)**

---

### **Faza 3: Ulepszanie doświadczeń graczy**

1. **System moralności i reputacji**:
   - Decyzje graczy wpływają na reputację i relacje z NPC. **(NIE ZACZĘTO)**
   - Fabuła zmienia się dynamicznie na podstawie wyborów. **(NIE ZACZĘTO)**

2. **Wielowątkowe narracje**:
   - Wielowarstwowe misje i wątki poboczne. **(NIE ZACZĘTO)**
   - Długoterminowy postęp fabularny. **(NIE ZACZĘTO)**

3. **System osiągnięć**:
   - Nagrody za specjalne osiągnięcia (np. pokonanie trudnych wrogów, odkrywanie ukrytych lokacji). **(NIE ZACZĘTO)**

4. **Zaawansowana interakcja z fabułą**:
   - NPC pamiętają działania graczy. **(NIE ZACZĘTO)**
   - Fabuła rozwija się na podstawie przeszłych decyzji. **(NIE ZACZĘTO)**

---

### **Faza 4: Multimedia i zanurzenie w grze**

1. **Efekty dźwiękowe i muzyka**:
   - Dynamiczna muzyka zależna od lokalizacji i wydarzeń (np. bitwy, eksploracja). **(NIE ZACZĘTO)**
   - Efekty dźwiękowe dla działań (np. otwieranie skrzyni, uderzenie w walce). **(NIE ZACZĘTO)**

2. **Ilustracje i grafika**:
   - Wizualne reprezentacje lokacji, NPC i wydarzeń. **(NIE ZACZĘTO)**
   - Personalizowane awatary dla postaci graczy. **(NIE ZACZĘTO)**

---

### **Faza 5: Funkcje społecznościowe i społecznościowe**

1. **Czat głosowy i tekstowy**:
   - Wbudowany system czatu dla komunikacji między graczami. **(ZROBIONE - tylko tekstowy)**
2. **Rankingi i rywalizacja**:
   - Punkty za ukończone scenariusze. **(NIE ZACZĘTO)**
   - Porównywanie wyników drużyn na tablicach wyników. **(NIE ZACZĘTO)**

3. **Hosting i skalowanie**:
   - Hosting backendu i frontendu w chmurze (np. AWS, DigitalOcean). **(NIE ZACZĘTO)**
   - Skalowanie serwerów do obsługi dużej liczby graczy. **(NIE ZACZĘTO)**

---

### **Faza 6: Testowanie i optymalizacja**

1. **Testowanie**:
   - Testy automatyczne funkcjonalności. **(ZROBIONE)**
   - Testowanie interakcji użytkowników z kreatorem scenariuszy i rozgrywką. **(NIE ZACZĘTO)**
   - Testowanie wydajności pod kątem skalowalności. **(NIE ZACZĘTO)**

2. **Optymalizacja**:
   - Udoskonalenie kodu frontendowego i backendowego pod kątem wydajności. **(NIE ZACZĘTO)**
   - Dostosowanie algorytmów do interakcji z dużą liczbą użytkowników. **(NIE ZACZĘTO)**

---

### **Aktualizacja: Dodanie czatu do aplikacji**

1. **Czat w poczekalni po zalogowaniu**:
   - Czat dla graczy czekających w poczekalni przed rozpoczęciem gry. **(ZROBIONE)**
   - Wykorzystanie WebSocketów do komunikacji w czasie rzeczywistym. **(ZROBIONE)**
   - Rozwijanie interfejsu czatu z emoji i opcją dodawania prywatnych wiadomości. **(NIE ZACZĘTO)**

--- 

