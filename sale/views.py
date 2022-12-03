from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from core.pagination import ResultSetPagination
from product.models import Product
from commission.models import Commission
from sale.models import Sale, SaleProduct
from sale.serializers import (
    SaleModelSerializer,
    SaleProductModelSerializer,
)
from sale.filters import SaleFilter
import datetime as dt


class SaleListCreateView(ListCreateAPIView):
    '''
    get:
    List the sales.

    post:
    Create a new sale.
    '''
    queryset = Sale.objects.all()
    serializer_class = SaleModelSerializer
    pagination_class = ResultSetPagination
    filter_backends = [SaleFilter]

    def get_commission_value(self):
        dtime = dt.datetime.now()
        weekday = dtime.weekday()

        commission = Commission.objects.get(week_day=weekday)

        return commission

    def create_sale_product_items(self, sale_id, products):
        for product in products:
            saleProduct = SaleProduct(
                sale_id=sale_id,
                product_id=product['id'],
                quantity=product['quantity'])
            saleProduct.save()

    def create(self, request, *args, **kwargs):

        commission = self.get_commission_value

        if not commission:
            request.data['commission_min'] = commission.commission_min
            request.data['commission_max'] = commission.commission_max

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        sale_instance = serializer.save()

        self.create_sale_product_items(
            sale_instance.id, request.data['productsListed'])

        return Response(status=status.HTTP_201_CREATED)


class SaleRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    '''
    get:
    Retrieve a sale.

    put:
    Update a sale.

    patch:
    Partially update a sale.

    delete:
    Delete a sale.
    '''
    queryset = Sale.objects.all()
    serializer_class = SaleModelSerializer
    lookup_field = 'id'


class SaleAddUpdateDeleteProductView(CreateModelMixin,
                                     UpdateModelMixin,
                                     DestroyModelMixin,
                                     APIView):
    '''
    post:
    Add a new product to a sale.
    '''
    serializer = SaleModelSerializer
    input_serializer = SaleProductModelSerializer
    sale_queryset = Sale.objects.all()
    product_queryset = Product.objects.all()

    def inject_sale_product(self, request: Request, **kwargs):
        request.data['sale'] = kwargs.get('sale_id')
        request.data['product'] = kwargs.get('product_id')

    def get_object(self) -> SaleProduct:
        filter_kwargs = {
            'sale': self.kwargs['sale_id'],
            'product': self.kwargs['product_id']
        }
        obj = get_object_or_404(SaleProduct, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs) -> SaleProduct:
        '''Create a SaleProduct instance.'''
        self.inject_sale_product(request, **kwargs)
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance: SaleProduct = serializer.save()
        serializer = self.serializer(instance.sale)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def update(self, request, *args, **kwargs):
        '''update a SaleProduct instance.'''
        self.inject_sale_product(request, **kwargs)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.input_serializer(instance,
                                           data=request.data,
                                           partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(self.serializer(instance.sale).data)

    def post(self, request: Request, *args, **kwargs) -> Response:
        return self.create(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs) -> Response:
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs) -> Response:
        return self.destroy(request, *args, **kwargs)
