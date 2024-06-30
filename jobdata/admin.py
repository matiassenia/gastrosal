
# Register your models here.
from django.contrib import admin
from .models import JobData

class JobDataAdmin(admin.ModelAdmin):
    list_display = ('position', 'formatted_salary', 'currency', 'contract_type', 'restaurant_name', 'gender')
    search_fields = ('position', 'restaurant_name')
    list_filter = ('currency', 'contract_type', 'gender')
    
