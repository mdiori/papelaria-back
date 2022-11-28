from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from core.pagination import ResultSetPagination
from client.serializers import ClientSerializer
from client.filters import ClientFilter
from client.models import Client


class ClientListCreateView(ListCreateAPIView):
    '''
    get:
    List the clients.

    post:
    Create a new client.
    '''
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = ResultSetPagination
    filter_backends = [ClientFilter]


class ClientRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    '''
    get:
    Retrieve a client.

    put:
    Update a client.

    patch:
    Partially a client.

    delete:
    Deletes a client.
    '''
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'
