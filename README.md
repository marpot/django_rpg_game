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

### Docker Integration

To simplify the setup and management of both backend and frontend containers, you can use the provided `Makefile` commands. Here are the common commands:

#### Start Containers

To start the containers in the background:

```bash
make up
```

#### Stop Containers

To stop the containers:

```bash
make down
```

#### Build Containers

To rebuild the containers:

```bash
make build
```

#### View Logs

To view the logs of the containers in real-time:

```bash
make logs
```

#### Restart Project

To restart the project (stop, build, start, and view logs):

```bash
make restart
```

#### Access Backend (Django) Container

To enter the backend (Django) container:

```bash
make backend
```

#### Access Frontend (React) Container

To enter the frontend (React) container:

```bash
make frontend
```

#### Django Migrations

To apply Django migrations:

```bash
make migrate
```

#### Generate Django Migrations

To generate Django migrations:

```bash
make makemigrations
```

#### Collect Static Files (Django)

To collect static files in Django:

```bash
make collectstatic
```

#### Create Django Superuser

To create a Django superuser:

```bash
make createsuperuser
```

#### Backend Testing

To run backend tests:

```bash
make test-backend
```

#### Frontend Testing

To run frontend tests:

```bash
make test-frontend
```

#### View Container Status

To view the status of the containers:

```bash
make ps
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
```