import random
from django.core.management.base import BaseCommand
from employee.models import Employee
import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Seed example employees."

    def handle(self, *args, **options):
        self.stdout.write('Seeding employee data...')
        run_seed(self)
        self.stdout.write('Done.')


def create_employee():
    logger.info("Creating employees:")

    names = []
    for x in range(0, 20):
        employee = Employee(
            name=f'Vendedor {x + 1}',
            mail=f'email{x + 1}@papelaria.com',
            phone=random.randint(111111111, 999999999),
            active=True
        )
        employee.save()

    logger.info("Employees created.")
    return


def run_seed(self):
    create_employee()
