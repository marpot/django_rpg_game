FROM python:3.10-slim

# Instalacja bash
RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Kopiowanie i instalacja zależności
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary

# Kopiowanie całej aplikacji
COPY . /app/

# Zbieranie statycznych plików
RUN python manage.py collectstatic --noinput

# Eksponowanie portu 8000
EXPOSE 8000

# Użycie entrypoint.sh
CMD ["./entrypoint.sh"]
