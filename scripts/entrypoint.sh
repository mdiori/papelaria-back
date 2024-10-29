#!/bin/sh

# Concede permissão de execução para o próprio script
chmod +x /app/scripts/entrypoint.sh

echo "Waiting for PostgreSQL to start..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

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

echo "-----> Starting server"
python manage.py runserver 0.0.0.0:8000
