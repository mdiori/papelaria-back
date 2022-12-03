from django.core.management.base import BaseCommand
from commission.models import Commission
import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Seed week days with default commission values."

    def handle(self, *args, **options):
        self.stdout.write('Seeding commission data...')
        run_seed(self)
        self.stdout.write('Done.')


def create_commission():
    logger.info("Creating commissions:")

    names = []
    for x in range(0, 7):
        commission = Commission(
            week_day=x,
            commission_min=0,
            commission_max=10000,
        )
        commission.save()

    logger.info("Commissions created.")
    return


def run_seed(self):
    create_commission()
