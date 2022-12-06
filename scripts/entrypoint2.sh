echo "-----> Making migrations"
python3 manage.py makemigrations

echo "-----> Migrating"
python3 manage.py migrate

echo "-----> Creating super user"
python3 manage.py shell < scripts/create_user.py

echo "-----> Seeding database"
python3 manage.py seedCommissions
python3 manage.py seedClients
python3 manage.py seedEmployees
python3 manage.py seedProducts
