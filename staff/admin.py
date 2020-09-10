from django.contrib import admin

from .models import Occupation

@admin.register(Occupation)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'position_name')
