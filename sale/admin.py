from django.contrib import admin
from sale.models import Sale, SaleProduct

class SaleAdmin(admin.ModelAdmin):
    list_display = ('formatted_date', 'client_name', 'employee_name', 'commission_range', 'invoice')
    list_filter = ('date', 'client', 'employee')
    search_fields = ('invoice', 'client__name', 'employee__name')

    def formatted_date(self, obj):
        return obj.date.strftime('%d/%m/%Y')
    formatted_date.short_description = 'Data'

    def client_name(self, obj):
        return obj.client.name
    client_name.short_description = 'Cliente'

    def employee_name(self, obj):
        return obj.employee.name
    employee_name.short_description = 'Vendedor'

    def commission_range(self, obj):
        return f"{obj.commission_min} - {obj.commission_max}"
    commission_range.short_description = 'Intervalo de Comissão'

admin.site.register(Sale, SaleAdmin)
