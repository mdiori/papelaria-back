echo "-----> Making migrations"
python manage.py makemigrations

echo "-----> Migrating"
python manage.py migrate

echo "-----> Creating super user"
python manage.py shell < scripts/create_user.py

echo "-----> Seeding database"
python manage.py seedCommissions
python manage.py seedClients
python manage.py seedEmployees
python manage.py seedProducts
