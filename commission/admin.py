from django.contrib import admin
from commission.models import Commission

class CommissionAdmin(admin.ModelAdmin):
    list_display = ('get_week_day_display', 'commission_min', 'commission_max')
    list_filter = ('week_day',)
    search_fields = ('commission_min', 'commission_max')

    """ def get_week_day_display(self, obj):
        return obj.get_week_day_display()
    get_week_day_display.short_description = 'Dia da Semana' """
    
    def get_week_day_display(self, obj):
        dias_semana = {
            0: "Segunda-feira",
            1: "Terça-feira",
            2: "Quarta-feira",
            3: "Quinta-feira",
            4: "Sexta-feira",
            5: "Sábado",
            6: "Domingo"
        }
        return dias_semana.get(obj.week_day, "Desconhecido")

admin.site.register(Commission, CommissionAdmin)
