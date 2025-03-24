# RPG Game Documentation

## Polish Documentation

### Backend
- [Dokumentacja Backendu](pl/backend/README.md)
- [Dokumentacja API](pl/api/README.md)

### Frontend
- [Dokumentacja Frontendu](pl/frontend/README.md)

## English Documentation

### Backend
- [Backend Documentation](en/backend/README.md)
- [API Documentation](en/api/README.md)

### Frontend
- [Frontend Documentation](en/frontend/README.md)

## Project Overview

This is a text-based RPG game built with Django and React. The game features:

- User authentication and authorization
- Character creation and management
- Game sessions and progress tracking
- Real-time chat functionality
- Event-based gameplay system
- Responsive web interface

## Quick Start

1. Clone the repository
2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   python manage.py migrate
   daphne -b 0.0.0.0 -p 8000 rpg_project.asgi:application
   ```

3. Set up the frontend:
   ```bash
   cd frontend
   npm install
   npm start
   ```

4. Access the application at `http://localhost:3000`

## Contributing

Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
