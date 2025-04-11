#!/bin/sh

echo "Sprawdzam dostępność bazy danych..." | tee -a /var/log/entrypoint.log
./wait-for-it.sh db:5432 --timeout=180 --strict -- echo "Baza danych gotowa!" | tee -a /var/log/entrypoint.log
if [ $? -eq 0 ]; then
  echo "Uruchamiam migracje bazy danych..." | tee -a /var/log/entrypoint.log
  python /app/manage.py migrate --noinput 2>&1 | tee -a /var/log/entrypoint.log
  if [ $? -ne 0 ]; then
    echo "Błąd migracji bazy danych!" | tee -a /var/log/entrypoint.log
    exit 1
  fi
else
  echo "Baza danych niedostępna, zatrzymuję kontener..." | tee -a /var/log/entrypoint.log
  exit 1
fi

echo "Uruchamiam Daphne..." | tee -a /var/log/entrypoint.log
daphne -b 0.0.0.0 -p 8000 rpg_project.asgi:application 2>&1 | tee -a /var/log/entrypoint.log
if [ $? -ne 0 ]; then
  echo "Błąd uruchamiania Daphne!" | tee -a /var/log/entrypoint.log
  exit 1
fi

# Usuń tail -f /dev/null, ponieważ Daphne powinien utrzymać kontener aktywnym
