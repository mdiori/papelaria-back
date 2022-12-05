from django.test import TestCase
from product.models import Product


class ProductModelTestCase(TestCase):

    def setUp(self):
        self.product = Product(
            name='Papel',
            description='Limitless paper in a paperless world',
            value=2000,
            commission=1000,
            code='1234',
            active=True
        )

    def test_to_verify_model_fields(self):
        self.assertEqual(self.product.name, 'Papel')
        self.assertEqual(self.product.description,
                         'Limitless paper in a paperless world')
        self.assertEqual(self.product.value, 2000)
        self.assertEqual(self.product.commission, 1000)
        self.assertEqual(self.product.code, '1234')
        self.assertEqual(self.product.active, True)
