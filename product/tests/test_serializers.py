from django.test import TestCase
from product.models import Product
from product.serializers import ProductSerializer


class ProductSerializerTestCase(TestCase):

    def setUp(self):
        self.product = Product(
            name='Papel',
            description='Limitless paper in a paperless world',
            value=2000,
            commission=1000,
            code='1234',
            active=True
        )

        self.serializer = ProductSerializer(instance=self.product)

    def test_to_verify_fields_serialization(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys(
        )), set(['id', 'name', 'description', 'value', 'commission', 'code', 'active', 'created_at', 'updated_at']))

    def test_to_verify_fields_serialization_values(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.product.name)
        self.assertEqual(data['description'], self.product.description)
        self.assertEqual(data['value'], self.product.value)
        self.assertEqual(data['commission'], self.product.commission)
        self.assertEqual(data['code'], self.product.code)
        self.assertEqual(data['active'], self.product.active)
        self.assertEqual(data['created_at'], self.product.created_at)
        self.assertEqual(data['updated_at'], self.product.updated_at)
