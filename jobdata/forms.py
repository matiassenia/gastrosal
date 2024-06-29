from django import forms
from .models import JobData

class JobDataForm(forms.ModelForm):
    class Meta:
        model = JobData
        fields = ['position', 'currency', 'salary', 'contract_type', 'restaurant_name', 'gender',]
        labels = {
            'position': 'Posición de Empleo',
            'currency': 'Moneda',
            'salary': 'Salario',
            'contract_type': 'Tipo de Contrato',
            'restaurant_name': 'Nombre del Restaurante/Establecimiento',
            'gender': 'Género',
        }
