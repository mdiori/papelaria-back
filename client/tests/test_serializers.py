from django.test import TestCase
from client.models import Client
from client.serializers import ClientSerializer


class ClientSerializerTestCase(TestCase):

    def setUp(self):
        self.client = Client(
            name='Matheus Diori',
            mail='mdiori@hotmail.com',
            phone='43996627041',
            active=True,
        )

        self.serializer = ClientSerializer(instance=self.client)

    def test_to_verify_fields_serialization(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys(
        )), set(['id', 'name', 'mail', 'phone', 'active', 'created_at', 'updated_at']))

    def test_to_verify_fields_serialization_values(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.client.name)
        self.assertEqual(data['mail'], self.client.mail)
        self.assertEqual(data['phone'], self.client.phone)
        self.assertEqual(data['active'], self.client.active)
        self.assertEqual(data['created_at'], self.client.created_at)
        self.assertEqual(data['updated_at'], self.client.updated_at)
