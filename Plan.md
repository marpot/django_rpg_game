### **Polska wersja:**

# Gra RPG

## Opis projektu

Jest to gra RPG, w której gracze mogą się logować, rejestrować, tworzyć pokoje i wchodzić w interakcje z fabułą. Gracze podejmują decyzje, które wpływają na rozwój fabuły. Gra jest zaprojektowana jako dynamiczna i interaktywna, oferująca kreatora scenariuszy dla bogatego opowiadania historii i rozgrywki.

## Plan tworzenia gry RPG z kreatorem scenariuszy

### **Faza 1: Budowanie fundamentów**
1. **Backend: Django REST Framework**
   - **Autentykacja i zarządzanie użytkownikami**:
     - Rejestracja i logowanie użytkowników z autentykacją JWT. **(ZROBIONE)**
     - Profile graczy. **(ZROBIONE)**
   - **Modele bazy danych**:
     - **User**: Dane gracza. **(ZROBIONE)**
     - **Room**: Pokój gry (scenariusz, status, gracze).
     - **PlayerCharacter**: Postać gracza (statystyki, ekwipunek). *(Aktualnie tylko poziom w modelach)*
     - **GameEvent**: Historia zdarzeń w grze.
   - **API**:
     - Rejestracja i logowanie. **(ZROBIONE)**
     - Tworzenie i dołączanie do pokoi.
     - Obsługa działań graczy w grze.

   - **Testowanie automatyczne Backend**:
     - Testowanie punktów końcowych, autentykacji i walidacji danych.

2. **Frontend: JavaScript**
   - **UI logowania i rejestracji**:
     - Stylizowany panel logowania. **(ZROBIONE)**
     - Wyświetlanie listy pokoi gry. (ZROBIONE)
     - Tworzenie pokoi.
   - **UI gry**:
     - Interfejs rozgrywki:
       - Wyświetlanie historii wydarzeń.
       - Wybory gracza i interakcje.

3. **Kreator scenariusza**:
   - **Predefiniowane scenariusze fabularne**:
     - Tworzenie wielu gałęzi fabuły.
   - **System zasad interakcji**:
     - Określenie jak wybory graczy wpływają na fabułę.
   - **Postęp fabuły**:
     - Generowanie wyników na podstawie decyzji graczy.

4. **Komunikacja w czasie rzeczywistym**:
   - WebSockets (Django Channels):
     - Obsługa wymiany danych w czasie rzeczywistym między graczami i systemem.
     - Synchronizacja działań graczy.

---

### **Faza 2: Rozszerzenie mechaniki rozgrywki**
1. **Współpraca graczy i interakcja**:
   - Wspólne zadania i decyzje.
   - Handel przedmiotami i wzajemne wsparcie w walce.

2. **System walki**:
   - **Mechanika turowa**:
     - Gracze wybierają akcje (atak, obrona, użycie umiejętności).
     - Wyniki określane przez zasady systemu.
   - **Statusy i efekty specjalne**:
     - "Zatruty", "Zamrożony", "Wzmocniony".
   - **Siatka taktyczna (opcjonalnie)**:
     - Możliwość poruszania się po siatce w czasie walki.

3. **Eksploracja i mapa świata**:
   - Mapa z dynamicznie generowanymi lokacjami.
   - Eksploracja przez graczy:
     - Wchodzenie do różnych lokacji.
     - Odkrywanie skarbów i sekretów.

4. **Unikalne postacie graczy**:
   - Zaawansowany kreator postaci:
     - Wybór rasy, klasy, umiejętności.
   - Rozwój postaci:
     - Zbieranie punktów doświadczenia i rozwój umiejętności.
     - Zarządzanie ekwipunkiem i przedmiotami.

---

### **Faza 3: Ulepszanie doświadczeń graczy**
1. **System moralności i reputacji**:
   - Decyzje graczy wpływają na reputację i relacje z NPC.
   - Fabuła zmienia się dynamicznie na podstawie wyborów.

2. **Wielowątkowe narracje**:
   - Wielowarstwowe misje i wątki poboczne.
   - Długoterminowy postęp fabularny.

3. **System osiągnięć**:
   - Nagrody za specjalne osiągnięcia (np. pokonanie trudnych wrogów, odkrywanie ukrytych lokacji).

4. **Zaawansowana interakcja z fabułą**:
   - NPC pamiętają działania graczy.
   - Fabuła rozwija się na podstawie przeszłych decyzji.

---

### **Faza 4: Multimedia i zanurzenie w grze**
1. **Efekty dźwiękowe i muzyka**:
   - Dynamiczna muzyka zależna od lokalizacji i wydarzeń (np. bitwy, eksploracja).
   - Efekty dźwiękowe dla działań (np. otwieranie skrzyni, uderzenie w walce).

2. **Ilustracje i grafika**:
   - Wizualne reprezentacje lokacji, NPC i wydarzeń.
   - Personalizowane awatary dla postaci graczy.

---

### **Faza 5: Funkcje społecznościowe i społecznościowe**
1. **Czat głosowy i tekstowy**:
   - Wbudowany system czatu dla komunikacji między graczami.
2. **Rankingi i rywalizacja**:
   - Punkty za ukończone scenariusze.
   - Porównywanie wyników drużyn na tablicach wyników.

3. **Hosting i skalowanie**:
   - Hosting backendu i frontendu w chmurze (np. AWS, DigitalOcean).
   - Skalowanie serwerów do obsługi dużej liczby graczy.

---

### **Faza 6: Testowanie i optymalizacja**
1. **Testowanie**:
   - Testy automatyczne funkcjonalności.
   - Testowanie interakcji użytkowników z kreatorem scenariuszy i rozgrywką.
   - Testowanie wydajności pod kątem skalowalności.

2. **Optymalizacja**:
   - Udoskonalenie kodu frontendowego i backendowego pod kątem wydajności.
   - Dostosowanie algorytmów do interakcji z dużą liczbą użytkowników.

---

### **Aktualizacja: Dodanie czatu do aplikacji**
1. **Czat w poczekalni po zalogowaniu**:
   - Czat dla graczy czekających w poczekalni przed rozpoczęciem gry.
   - Wykorzystanie WebSocketów do komunikacji w czasie rzeczywistym.
   - Rozwijane okno czatu po prawej stronie.

2. **Czat w pokoju gry**:
   - Czat dedykowany dla graczy w danym pokoju gry.
   - Komunikacja w czasie rzeczywistym za pomocą WebSocketów.
   - Stylizowanie okna czatu po prawej stronie ekranu.

---

### **Technologie użyte**

- **Backend**: Django, Django REST Framework
- **Frontend**: React
- **Autentykacja**: JWT (JSON Web Tokens)
- **Baza danych**: SQLite (może zostać zmieniona na PostgreSQL w produkcji)
- **WebSocket**: Django Channels (do komunikacji w czasie rzeczywistym)

---

### **Instrukcje instalacji**

**Backend (Django)**

1. Zainstaluj wymagane pakiety:

```bash
pip install -r requirements.txt
```

2. Zastosuj migracje bazy danych:

```bash
python manage.py migrate
```

3. Uruchom serwer backendu:

```bash
python manage.py runserver
```

**Frontend (React)**

1. Zainstaluj wymagane pakiety:

```bash
npm install
```

2. Uruchom aplikację frontendową:

```bash
npm start
```

---

**Współpraca**

Jeśli chcesz przyczynić się do projektu:

1. Sklonuj repozytorium.
2. Stwórz nową gałąź (`git checkout -b feature/my-feature`).
3. Wprowadź zmiany i zapisz je.
4. Wypchnij zmiany do swojego repozytorium (`git push origin feature/my-feature`).
5. Stwórz pull request.

---

**Licencja**

Projekt jest licencjonowany na podstawie [Licencji MIT](LICENSE).

---

**Autorzy**

- Marcin Potoczny

---

### **English Version:**

# RPG Game

## Project Description

This project is an RPG game where players can log in, register, create rooms, and interact with the storyline. Players make decisions that impact the development of the plot. The game is designed to be dynamic and interactive, offering a

 scenario creator for rich storytelling and gameplay.

## Plan for Creating the RPG Game with Scenario Creator

### **Phase 1: Building the Foundations**
1. **Backend: Django REST Framework**
   - **Authentication and User Management**:
     - User registration and login with JWT authentication. **(DONE)**
     - Player profiles. **(DONE)**
   - **Database Models**:
     - **User**: Player data. **(DONE)**
     - **Room**: Game room (scenario, status, players).
     - **PlayerCharacter**: Player's character (stats, inventory). *(Currently only level in models)*
     - **GameEvent**: History of in-game events.
   - **API**:
     - Registration and login. **(DONE)**
     - Room creation and joining.
     - Handling player actions in the game.

   - **Automated Backend Testing**:
     - Test endpoints, authentication, and data validation.

2. **Frontend: JavaScript**
   - **Login and Registration UI**:
     - Styled login panel. **(DONE)**
     - Display a list of game rooms.
     - Room creation.
   - **Game UI**:
     - Interface for gameplay:
       - Event history display.
       - Player choices and interactions.

3. **Scenario Creator**:
   - **Predefined story scenarios**:
     - Create multiple branching storylines.
   - **Interaction rule system**:
     - Define how player choices impact the storyline.
   - **Story progression**:
     - Generate outcomes based on player decisions.

4. **Real-Time Communication**:
   - WebSockets (Django Channels):
     - Handle real-time data exchange between players and the system.
     - Synchronize player actions.

---

### **Phase 2: Expanding Gameplay Mechanics**
1. **Player Collaboration and Interaction**:
   - Joint tasks and decisions.
   - Item trading and mutual support in combat.

2. **Combat System**:
   - **Turn-based mechanics**:
     - Players select actions (attack, defend, use skills).
     - Outcomes determined by system rules.
   - **Statuses and special effects**:
     - "Poisoned," "Frozen," "Boosted."
   - **Tactical grid (optional)**:
     - Allow movement on a grid during combat.

3. **Exploration and World Map**:
   - Map with dynamically generated locations.
   - Exploration by players:
     - Entering various locations.
     - Discovering treasures and secrets.

4. **Unique Player Characters**:
   - Advanced character creator:
     - Choose race, class, abilities.
   - Character development:
     - Earn experience points and level up skills.
     - Manage inventory and items.

---

### **Phase 3: Enhancing the Game Experience**
1. **Morality and Reputation System**:
   - Player decisions affect reputation and relationships with NPCs.
   - The storyline changes dynamically based on choices.

2. **Multi-threaded Narratives**:
   - Multi-layered quests and side stories.
   - Long-term storyline progression.

3. **Achievement System**:
   - Rewards for special accomplishments (e.g., defeating tough enemies, exploring hidden locations).

4. **Advanced Scenario Interaction**:
   - NPCs remember player actions.
   - Storylines evolve based on past decisions.

---

### **Phase 4: Multimedia and Immersion**
1. **Sound Effects and Music**:
   - Dynamic music based on location and events (e.g., battles, exploration).
   - Sound effects for actions (e.g., opening a chest, striking in combat).

2. **Illustrations and Graphics**:
   - Visual representations of locations, NPCs, and events.
   - Personalized avatars for player characters.

---

### **Phase 5: Social and Community Features**
1. **Voice and Text Chat**:
   - Built-in chat system for player communication.
2. **Rankings and Competition**:
   - Points for completing scenarios.
   - Compare team performance in leaderboards.

3. **Hosting and Scaling**:
   - Host backend and frontend in the cloud (e.g., AWS, DigitalOcean).
   - Scale servers to handle a large player base.

---

### **Phase 6: Testing and Optimization**
1. **Testing**:
   - Automated functional tests.
   - Test user interaction with the scenario creator and gameplay.
   - Performance testing for scalability.

2. **Optimization**:
   - Refine frontend and backend code for better performance.
   - Adapt algorithms for large-scale user interactions.

---

### **Update: Adding Chat Features**
1. **Waiting Room Chat After Login**:
   - A chat system for players waiting in the lobby before the game starts.
   - Real-time communication using WebSockets.
   - Expandable chat window on the right side.

2. **In-Room Chat During Gameplay**:
   - A chat dedicated to players in a specific game room.
   - Real-time communication using WebSockets.
   - Chat window styled on the right side of the screen.

---

### **Technologies Used**

- **Backend**: Django, Django REST Framework
- **Frontend**: React
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: SQLite (may switch to PostgreSQL for production)
- **WebSocket**: Django Channels (for real-time communication)

---

### **Installation Instructions**

**Backend (Django)**

1. Install required packages:

```bash
pip install -r requirements.txt
```

2. Apply database migrations:

```bash
python manage.py migrate
```

3. Run backend server:

```bash
python manage.py runserver
```

**Frontend (React)**

1. Install required packages:

```bash
npm install
```

2. Run frontend app:

```bash
npm start
```

---

**Collaboration**

If you want to contribute to the project:

1. Clone the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make changes and commit them.
4. Push changes to your repository (`git push origin feature/my-feature`).
5. Create a pull request.

---

**License**

This project is licensed under the [MIT License](LICENSE).

---

**Authors**

- Marcin Potoczny