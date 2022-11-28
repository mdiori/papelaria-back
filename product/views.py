from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from core.pagination import ResultSetPagination
from product.serializers import ProductSerializer
from product.filters import ProductFilter
from product.models import Product


class ProductListCreateView(ListCreateAPIView):
    '''
    get:
    List the products.

    post:
    Create a new product.
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ResultSetPagination
    filter_backends = [ProductFilter]


class ProductRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    '''
    get:
    Retrieve a product.

    put:
    Update a product.

    patch:
    Partially a product.

    delete:
    Deletes a product.
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
