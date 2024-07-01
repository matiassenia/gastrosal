
from django.contrib import admin
from .models import JobData

# Definimos una clase personalizada para la administración del modelo JobData
class JobDataAdmin(admin.ModelAdmin):
    list_display = ('position', 'formatted_salary', 'currency', 'contract_type', 'restaurant_name', 'gender') # Especificamos los campos que queremos mostrar en la lista de objetos en el panel de administración
    list_filter = ('position', 'currency', 'contract_type', 'gender') # Añadimos filtros laterales para los campos que seleccionamos
    search_fields = ('position', 'restaurant_name') # Habilitamos un campo de búsqueda para los campos position y restaurant_name
    ordering = ('position',) # Ordenamos los resultados por el campo position

    # Definimos un método para formatear el campo salary con puntos como separadores de miles
    def formatted_salary(self, obj):
        return f'{obj.salary:,.0f}'.replace(',', '.') # Convertimos el salario a una cadena con separadores de miles y reemplazamos comas con puntos
    formatted_salary.short_description = 'Salario' # Cambiamos la etiqueta de este campo en la interfaz de administración
    
admin.site.register(JobData, JobDataAdmin) # Registramos nuestro modelo JobData y la configuración personalizada JobDataAdmin en el panel de administración
