Jasne! Oto zaktualizowany `README.md`, który uwzględnia zarówno opis projektu RPG, jak i nowe informacje dotyczące kontenerów Docker i użycia `Makefile`. Dodałem sekcję dotyczącą developmentu z Dockerem, opis `Makefile` oraz uprościłem uruchamianie aplikacji przez polecenia `make`.

---

```markdown
# RPG Game

## Project Description

This project is an RPG game where players can log in, register, create rooms, and interact with the storyline. Players make decisions that impact the development of the plot. The game is designed to be dynamic and interactive.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: React
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: SQLite (may switch to PostgreSQL for production)
- **WebSocket**: Django Channels (for real-time communication)
- **Containerization**: Docker & Docker Compose
- **Dev tools**: Makefile for common commands

## Features

### Backend

1. **Player registration and login** using JWT.
2. **Player profiles** with editable data.
3. **Creating and joining game rooms**.
4. **Game model** with a history of events and player actions.

### Frontend

1. **Login and registration UI**.
2. **Dashboard** – view after login, access to game rooms.
3. **Gameplay interface** – displaying event history and player choices.

### Future Plans

1. **Scenario creator** – a tool for generating game scenarios.
2. **Combat system** and **player collaboration** features.
3. **Custom RPG-style dark UI** styled with SCSS.

## Development Setup (Docker + Makefile)

Make sure you have **Docker** and **Docker Compose** installed.

### Quick Start

```bash
make up        # Start containers
make down      # Stop containers
make logs      # View live logs
```

### Useful Commands

| Command               | Description                              |
|------------------------|------------------------------------------|
| `make build`           | Build all containers                     |
| `make restart`         | Rebuild and restart the entire project   |
| `make backend`         | Access backend container (Django)        |
| `make frontend`        | Access frontend container (React)        |
| `make migrate`         | Run Django database migrations           |
| `make makemigrations`  | Generate Django migration files          |
| `make collectstatic`   | Collect Django static files              |
| `make createsuperuser` | Create a Django superuser                |
| `make test-backend`    | Run backend tests                        |
| `make test-frontend`   | Run frontend tests                       |
| `make ps`              | Show container status                    |

## Manual Installation (without Docker)

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
daphne -b 0.0.0.0 -p 8000 rpg_project.asgi:application
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
2. Create a new branch:

```bash
git checkout -b feature/my-feature
```

3. Make changes and commit them.
4. Push changes to your fork:

```bash
git push origin feature/my-feature
```

5. Create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Authors

- Marcin Potoczny
`
## Architecture Diagram

          +---------------------+
          |     Frontend        |
          |  (React + SCSS)     |
          |---------------------|
          | Runs in Docker      |
          | Communicates via    |
          | HTTP/HTTPS (REST)   |
          +----------+----------+
                     |
                     v
          +---------------------+
          |      Backend        |
          |  (Django + DRF)     |
          |---------------------|
          | REST API & JWT Auth |
          | Django Channels     |
          | Runs in Docker      |
          +----------+----------+
                     |
    +----------------+----------------+
    |                                 |
    v                                 v

+------------------+ +---------------------+ | Database | | WebSockets Server | | (SQLite/PG) | | (Django Channels) | +------------------+ +---------------------+

Jeśli chcesz, mogę jeszcze dorzucić diagram architektury albo dodać przykład `.env.development`. Chcesz coś takiego?