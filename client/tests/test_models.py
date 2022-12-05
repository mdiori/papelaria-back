from django.test import TestCase
from client.models import Client


class ClientModelTestCase(TestCase):

    def setUp(self):
        self.client = Client(
            name='Matheus Diori',
            mail='mdiori@hotmail.com',
            phone='43996627041',
            active=True
        )

    def test_to_verify_model_fields(self):
        self.assertEqual(self.client.name, 'Matheus Diori')
        self.assertEqual(self.client.mail, 'mdiori@hotmail.com')
        self.assertEqual(self.client.phone, '43996627041')
        self.assertEqual(self.client.active, True)
