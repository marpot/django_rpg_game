Tak, dodanie planu projektu w języku angielskim do pliku `README.md` może być dobrym pomysłem, ponieważ pozwala potencjalnym współtwórcom zrozumieć kierunek, w którym zmierza projekt. Zaktualizuję plan w języku angielskim i odpowiednio go zaimplementuję w pliku `README.md`. Oto, jak mógłby wyglądać:

```markdown
# RPG Game

## Project Description

This project is an RPG game where players can log in, register, create rooms, and interact with the storyline. Players make decisions that impact the development of the plot. The game is designed to be dynamic and interactive, offering a scenario creator for rich storytelling and gameplay.

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

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: React
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: SQLite (may switch to PostgreSQL for production)
- **WebSocket**: Django Channels (for real-time communication)

## Installation

### Backend (Django)

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Apply database migrations:

```bash
python manage.py migrate
```

3. Run the backend server:

```bash
python manage.py runserver
```

### Frontend (React)

1. Install the required packages:

```bash
npm install
```

2. Run the frontend app:

```bash
npm start
```

## Collaboration

If you want to contribute to the project:

1. Clone the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Make changes and commit them.
4. Push changes to your repository (`git push origin feature/my-feature`).
5. Create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Authors

- Marcin Potoczny