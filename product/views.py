from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
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

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.filter(description=request.query_params.get(
            'description')).filter(code=request.query_params.get('code'))

        queryset = Product.objects.filter()

        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)


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
