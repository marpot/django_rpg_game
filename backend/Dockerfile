FROM python:3.10-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Instalacja zależności
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary

# Kopiowanie plików projektu
COPY . /app/

# Eksponowanie portu
EXPOSE 8000

# Uruchomienie serwera Daphne
CMD ["daphne", "-u", "/app/daphne.sock", "rpg_project.asgi:application"]
