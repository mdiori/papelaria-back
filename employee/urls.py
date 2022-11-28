from django.urls import path
from employee.views import (
    EmployeeListCreateView,
    EmployeeRetriveUpdateDestroyView,
)


urlpatterns = [
    path('',
         EmployeeListCreateView.as_view(),
         name='employee-list-create'),
    path('<uuid:id>/',
         EmployeeRetriveUpdateDestroyView.as_view(),
         name='employee-retrieve-update-destroy'),
]
