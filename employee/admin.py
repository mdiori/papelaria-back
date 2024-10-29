from django.contrib import admin
from employee.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'phone', 'active')

admin.site.register(Employee, EmployeeAdmin)
