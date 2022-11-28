from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from core.pagination import ResultSetPagination
from employee.serializers import EmployeeSerializer
from employee.filters import EmployeeFilter
from employee.models import Employee


class EmployeeListCreateView(ListCreateAPIView):
    '''
    get:
    List the employees.

    post:
    Create a new employee.
    '''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = ResultSetPagination
    filter_backends = [EmployeeFilter]


class EmployeeRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    '''
    get:
    Retrieve a employee.

    put:
    Update a employee.

    patch:
    Partially a employee.

    delete:
    Deletes a employee.
    '''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
