#!/bin/sh

echo "Waiting for PostgreSQL to start..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# Check if this is the first-time run
if [ ! -f "/app/.initialized" ]; then
    echo "-----> Making migrations"
    python manage.py makemigrations

    echo "-----> Migrating"
    python manage.py migrate

    echo "-----> Creating superuser"
    python manage.py shell < scripts/create_user.py

    echo "-----> Seeding database"
    python manage.py seedCommissions
    python manage.py seedClients
    python manage.py seedEmployees
    python manage.py seedProducts

    # Create a marker file to indicate initialization has been completed
    touch /app/.initialized
else
    echo "Initialization already completed. Skipping..."
fi

echo "-----> Starting server"
exec python manage.py runserver 0.0.0.0:8000
