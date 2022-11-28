from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from commission.models import Commission


class CommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commission
        fields = ['id', 'week_day', 'commission_min', 'commission_max',
                  'active', 'created_at', 'updated_at', ]
        read_only_fields = ['id', 'created_at', 'updated_at', ]
        extra_kwargs = {
            'week_day': {
                'validators': [
                    UniqueValidator(Commission.objects.all())
                ]
            },
        }
