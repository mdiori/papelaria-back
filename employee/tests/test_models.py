from django.test import TestCase
from employee.models import Employee


class EmployeeModelTestCase(TestCase):

    def setUp(self):
        self.employee = Employee(
            name='Matheus Diori',
            mail='mdiori@hotmail.com',
            phone='43996627041',
            active=True
        )

    def test_to_verify_model_fields(self):
        self.assertEqual(self.employee.name, 'Matheus Diori')
        self.assertEqual(self.employee.mail, 'mdiori@hotmail.com')
        self.assertEqual(self.employee.phone, '43996627041')
        self.assertEqual(self.employee.active, True)
