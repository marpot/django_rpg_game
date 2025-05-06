#!/bin/sh

echo "🕵️‍♂️ Sprawdzam dostępność bazy danych..." | tee -a /var/log/entrypoint.log

# Wykrywanie systemu operacyjnego
OS="$(uname | tr '[:upper:]' '[:lower:]')"

if echo "$OS" | grep -q "mingw\|msys\|cygwin"; then
  # Windows
  echo "🔍 Wykryto system Windows." | tee -a /var/log/entrypoint.log
  ./wait-for-it.bat db:5432 --timeout=180 --strict
else
  # Linux/macOS
  echo "🐧 Wykryto system Linux/macOS." | tee -a /var/log/entrypoint.log
  ./wait-for-it.sh db:5432 --timeout=180 --strict
fi

if [ $? -eq 0 ]; then
  echo "✅ Baza danych gotowa, uruchamiam migracje..." | tee -a /var/log/entrypoint.log
  python /app/manage.py migrate --noinput 2>&1 | tee -a /var/log/entrypoint.log
  if [ $? -ne 0 ]; then
    echo "❌ Błąd migracji bazy danych!" | tee -a /var/log/entrypoint.log
    exit 1
  fi
else
  echo "❌ Baza danych niedostępna, zatrzymuję kontener..." | tee -a /var/log/entrypoint.log
  exit 1
fi

echo "🚀 Uruchamiam Daphne..." | tee -a /var/log/entrypoint.log
daphne -b 0.0.0.0 -p 8000 rpg_project.asgi:application 2>&1 | tee -a /var/log/entrypoint.log
