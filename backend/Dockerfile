FROM python:3.10-slim

WORKDIR /app

# Kopiowanie plików i instalacja zależności
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary

COPY . /app/

# Wykonanie migracji i zebranie statycznych plików
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

# Eksponowanie portu
EXPOSE 8000

# Uruchomienie Daphne (WebSockets + HTTP)
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "rpg_project.asgi:application"]
