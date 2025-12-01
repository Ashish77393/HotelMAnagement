#!/bin/bash
set -e

# Wait-for-db helper could be added here for production
echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server: $@"
exec "$@"
