from django.test import TestCase
from sale.models import Sale
from sale.models import SaleProduct
from sale.serializers import SaleModelSerializer
from sale.serializers import SaleProductModelSerializer
from client.models import Client
from employee.models import Employee


class SaleSerializerTestCase(TestCase):

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
            employee=self.employee,
        )

        # self.saleProducts = SaleProduct(
        #     quantity=10,
        # )

        self.saleProducts = []

        self.serializer = SaleModelSerializer(instance=self.sale)

    def test_to_verify_fields_serialization(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys(
        )), set(['id', 'date', 'commission_min', 'commission_max', 'invoice', 'employee', 'client', 'sale_products']))

    def test_to_verify_fields_serialization_values(self):
        data = self.serializer.data
        self.assertEqual(data['date'], self.sale.date)
        self.assertEqual(data['commission_min'], self.sale.commission_min)
        self.assertEqual(data['commission_max'], self.sale.commission_max)
        self.assertEqual(data['invoice'], self.sale.invoice)
        self.assertEqual(data['sale_products'], self.saleProducts)
