#!/bin/sh

# Czekaj na dostępność bazy danych PostgreSQL
echo "Czekam na dostępność bazy danych PostgreSQL..."
/backend/wait-for-it.sh db:5432 --timeout=60 --strict -- echo "Baza danych jest gotowa!" || { echo "Baza danych jest niedostępna. Zatrzymuję skrypt."; exit 1; }

# Uruchom migracje bazy danych
echo "Uruchamiam migracje bazy danych..."
python /backend/manage.py migrate --noinput || { echo "Migracja bazy danych nie powiodła się."; exit 1; }

# Uruchom Daphne
echo "Uruchamiam Daphne..."
exec daphne -u /tmp/daphne.sock rpg_project.asgi:application || { echo "Uruchomienie Daphne nie powiodło się."; exit 1; }
