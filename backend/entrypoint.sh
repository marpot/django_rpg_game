#!/bin/sh

echo "Sprawdzam dostępność bazy danych..."
./wait-for-it.sh db:5432 --timeout=180 --strict -- echo "Baza danych gotowa!" | tee -a /var/log/entrypoint.log
if [ $? -eq 0 ]; then
  echo "Uruchamiam migracje bazy danych..."
  python /app/manage.py migrate --noinput || { echo "Błąd migracji bazy danych!" | tee -a /var/log/entrypoint.log; exit 1; }
else
  echo "Baza danych niedostępna, zatrzymuję kontener..." | tee -a /var/log/entrypoint.log
  exit 1
fi

echo "Uruchamiam Daphne..."
daphne -b 0.0.0.0 -p 8000 rpg_project.asgi:application || { echo "Błąd uruchamiania Daphne!" | tee -a /var/log/entrypoint.log; exit 1; }