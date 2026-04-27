#!/bin/sh
set -e

echo "🧠 Celery worker starting..."

exec celery -A rpg_project worker -l info