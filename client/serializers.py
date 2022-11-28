from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'mail', 'phone',
                  'active', 'created_at', 'updated_at', ]
        read_only_fields = ['id', 'created_at', 'updated_at', ]
        extra_kwargs = {
            'mail': {
                'validators': [
                    UniqueValidator(Client.objects.all())
                ]
            },
        }
