from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from sale.models import Sale, SaleProduct
from product.serializers import ProductSerializer
from client.serializers import ClientSerializer
from employee.serializers import EmployeeSerializer
from rest_framework.validators import UniqueValidator


class SaleProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleProduct
        fields = ['id', 'quantity', 'sale',
                  'product', 'created_at', 'updated_at', ]
        read_only_fields = ['id', 'created_at', 'updated_at', ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        expand_options = self.context.get('expand', [])

        if 'sale' in expand_options and instance.sale:
            rep['sale'] = SaleModelSerializer(instance.sale).data
            rep['sale'].pop('sale_products')

        if 'product' in expand_options and instance.product:
            rep['product'] = ProductSerializer(instance.product).data

        return rep


class SaleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'date', 'commission_min', 'client', 'employee',
                  'commission_max', 'invoice', ]
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'name': {
                'validators': [
                    UniqueValidator(Sale.objects.all())
                ]
            },
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep['client'] = ClientSerializer(
            instance.client
        ).data

        rep['employee'] = EmployeeSerializer(
            instance.employee
        ).data

        rep['sale_products'] = SaleProductModelSerializer(
            instance.saleproduct_set.all(),
            many=True,
            context={'expand': ['product']}
        ).data

        return rep
