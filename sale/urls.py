from django.urls import path
from sale.views import (
    SaleAddUpdateDeleteProductView,
    SaleListCreateView,
    SaleRetrieveUpdateDestroyView,
)


urlpatterns = [
    path('', SaleListCreateView.as_view(), name='sale-list-create'),
    path('<uuid:id>/',
         SaleRetrieveUpdateDestroyView.as_view(),
         name='sale-retrieve-update-destroy'),
    path('<uuid:sale_id>/product/<uuid:product_id>/',
         SaleAddUpdateDeleteProductView.as_view(),
         name='sale-product-add'),
]
