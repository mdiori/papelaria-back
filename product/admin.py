from django.contrib import admin
from product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description', 'value', 'commission', 'active')
    list_filter = ('active', 'commission')
    search_fields = ('name', 'code')
    ordering = ('code',)
    list_editable = ('active', 'commission')
    fields = ('code', 'name', 'description', 'value', 'commission', 'active')
