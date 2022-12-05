import random
from django.core.management.base import BaseCommand
from client.models import Client
import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Seed example clients."

    def handle(self, *args, **options):
        self.stdout.write('Seeding client data...')
        run_seed(self)
        self.stdout.write('Done.')


def create_client():
    logger.info("Creating clients:")

    names = []
    for x in range(0, 5):
        client = Client(
            name=f'Cliente {x + 1}',
            mail=f'email{x + 1}@papelaria.com',
            phone=random.randint(111111111, 999999999),
            active=True
        )
        client.save()

    logger.info("Clients created.")
    return


def run_seed(self):
    create_client()
