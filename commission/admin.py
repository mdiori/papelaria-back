from django.contrib import admin
from commission.models import Commission

class CommissionAdmin(admin.ModelAdmin):
    list_display = ('get_week_day_display', 'commission_min', 'commission_max')
    list_filter = ('week_day',)
    search_fields = ('commission_min', 'commission_max')

    def get_week_day_display(self, obj):
        """Exibe o dia da semana no formato legível."""
        return obj.get_week_day_display()
    get_week_day_display.short_description = 'Dia da Semana'

admin.site.register(Commission, CommissionAdmin)
