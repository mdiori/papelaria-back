from django.urls import path
from commission.views import (
    CommissionListCreateView,
    CommissionRetriveUpdateDestroyView,
)


urlpatterns = [
    path('',
         CommissionListCreateView.as_view(),
         name='commission-list-create'),
    path('<uuid:id>/',
         CommissionRetriveUpdateDestroyView.as_view(),
         name='commission-retrieve-update-destroy'),
]
