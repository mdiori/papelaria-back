from django.contrib import admin
from django.urls import path, include

API_PFX = 'api/v1.0'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{API_PFX}/product/', include('product.urls')),
]
