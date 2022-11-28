from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'value', 'commission', 'code',
                  'active', 'created_at', 'updated_at', ]
        read_only_fields = ['id', 'created_at', 'updated_at', ]
        extra_kwargs = {
            'code': {
                'validators': [
                    UniqueValidator(Product.objects.all())
                ]
            },
        }
