from decouple import config
from django.contrib.auth.models import User

superuser = User.objects.filter(username=config('SUPERUSER'))
if not superuser.exists():
    username = config('SUPERUSER')
    user_email = ''.join(username.strip().split(' '))
    User.objects.create_superuser(
        username=config('SUPERUSER'),
        email=f'{user_email}@email.org.br',
        password=config('SUPERUSER_PASS')
    )
