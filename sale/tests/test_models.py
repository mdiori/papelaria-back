from django.test import TestCase
from sale.models import Sale
from client.models import Client
from employee.models import Employee


class SaleModelTestCase(TestCase):

    def setUp(self):
        self.client = Client(
            name='Matheus Diori',
            mail='mdiori@hotmail.com',
            phone='43996627041',
            active=True
        )

        self.employee = Employee(
            name='Matheus Diori',
            mail='mdiori@hotmail.com',
            phone='43996627041',
            active=True
        )

        self.sale = Sale(
            date='2022-10-10',
            commission_min=0,
            commission_max=1000,
            invoice='1000',
            client=self.client,
            employee=self.employee
        )

    def test_to_verify_model_fields(self):
        self.assertEqual(self.sale.date, '2022-10-10')
        self.assertEqual(self.sale.commission_min, 0)
        self.assertEqual(self.sale.commission_max, 1000)
        self.assertEqual(self.sale.invoice, '1000')
        self.assertEqual(self.sale.client, self.client)
        self.assertEqual(self.sale.employee, self.employee)
