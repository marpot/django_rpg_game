#!/bin/sh
set -e

echo "🧠 Backend starting..."

echo "🔎 Waiting for DNS resolution of db..."

until getent hosts db; do
  echo "DNS not ready for db..."
  sleep 1
done

echo "⏳ Waiting for PostgreSQL..."

TIMEOUT=60
COUNTER=0

until PGPASSWORD=$POSTGRES_PASSWORD pg_isready -h db -p 5432 -U $POSTGRES_USER; do
  echo "PostgreSQL not ready yet..."
  sleep 2

  COUNTER=$((COUNTER + 2))

  if [ "$COUNTER" -ge "$TIMEOUT" ]; then
    echo "❌ Timeout waiting for PostgreSQL!"
    exit 1
  fi
done

echo "✅ PostgreSQL is ready!"

echo "📦 Running migrations..."
python manage.py migrate --noinput

if [ "$DJANGO_COLLECTSTATIC" = "1" ]; then
  echo "📦 Collecting static files..."
  python manage.py collectstatic --noinput
fi

echo "🚀 Starting Daphne..."
exec daphne -b 0.0.0.0 -p 8000 rpg_project.asgi:application