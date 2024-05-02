from django.contrib import admin

from computer.models import ComputerModel


@admin.register(ComputerModel)
class ComputerModelAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'model', 'year_of_creation', 'price']
    list_filter = ['company_name', 'model', 'year_of_creation']