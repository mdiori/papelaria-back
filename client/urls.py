from django.urls import path
from client.views import (
    ClientListCreateView,
    ClientRetriveUpdateDestroyView,
)


urlpatterns = [
    path('',
         ClientListCreateView.as_view(),
         name='client-list-create'),
    path('<uuid:id>/',
         ClientRetriveUpdateDestroyView.as_view(),
         name='client-retrieve-update-destroy'),
]
