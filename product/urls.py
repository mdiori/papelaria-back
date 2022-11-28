from django.urls import path
from product.views import (
    ProductListCreateView,
    ProductRetriveUpdateDestroyView,
)


urlpatterns = [
    path('',
         ProductListCreateView.as_view(),
         name='product-list-create'),
    path('<uuid:id>/',
         ProductRetriveUpdateDestroyView.as_view(),
         name='product-retrieve-update-destroy'),
]
