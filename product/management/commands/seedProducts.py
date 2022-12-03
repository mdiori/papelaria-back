import random
from django.core.management.base import BaseCommand
from product.models import Product
import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Seed example products."

    def handle(self, *args, **options):
        self.stdout.write('Seeding product data...')
        run_seed(self)
        self.stdout.write('Done.')


def create_product():
    logger.info("Creating products:")

    names = []
    for x in range(0, 20):
        product = Product(
            name=f'Produto {x + 1}',
            description=f'Descrição produto {x + 1}',
            value=random.randint(1, 10000),
            commission=random.randint(0, 10),
            code=random.randint(1, 10000),
            active=True
        )
        product.save()

    logger.info("Products created.")
    return


def run_seed(self):
    create_product()
