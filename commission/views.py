from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from core.pagination import ResultSetPagination
from commission.serializers import CommissionSerializer
from commission.filters import CommissionFilter
from commission.models import Commission


class CommissionListCreateView(ListCreateAPIView):
    '''
    get:
    List the commissions.

    post:
    Create a new commission.
    '''
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer
    pagination_class = ResultSetPagination
    filter_backends = [CommissionFilter]


class CommissionRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    '''
    get:
    Retrieve a commission.

    put:
    Update a commission.

    patch:
    Partially a commission.

    delete:
    Deletes a commission.
    '''
    queryset = Commission.objects.all()
    serializer_class = CommissionSerializer
    lookup_field = 'id'
