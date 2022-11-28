from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'mail', 'phone',
                  'active', 'created_at', 'updated_at', ]
        read_only_fields = ['id', 'created_at', 'updated_at', ]
        extra_kwargs = {
            'mail': {
                'validators': [
                    UniqueValidator(Employee.objects.all())
                ]
            },
        }
