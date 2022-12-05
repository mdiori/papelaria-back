from django.test import TestCase
from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeSerializerTestCase(TestCase):

    def setUp(self):
        self.employee = Employee(
            name='Matheus Diori',
            mail='mdiori@hotmail.com',
            phone='43996627041',
            active=True,
        )

        self.serializer = EmployeeSerializer(instance=self.employee)

    def test_to_verify_fields_serialization(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys(
        )), set(['id', 'name', 'mail', 'phone', 'active', 'created_at', 'updated_at']))

    def test_to_verify_fields_serialization_values(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.employee.name)
        self.assertEqual(data['mail'], self.employee.mail)
        self.assertEqual(data['phone'], self.employee.phone)
        self.assertEqual(data['active'], self.employee.active)
        self.assertEqual(data['created_at'], self.employee.created_at)
        self.assertEqual(data['updated_at'], self.employee.updated_at)
