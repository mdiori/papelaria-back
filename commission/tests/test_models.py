from django.test import TestCase
from commission.models import Commission


class CommissionModelTestCase(TestCase):

    def setUp(self):
        self.commission = Commission(
            week_day=4,
            commission_min=100,
            commission_max=1000,
        )

    def test_to_verify_model_fields(self):
        self.assertEqual(self.commission.week_day, 4)
        self.assertEqual(self.commission.commission_min, 100)
        self.assertEqual(self.commission.commission_max, 1000)
