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
        widgets = {
            'position': forms.Select(attrs={'class': 'form-control'}),
            'currency': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'placeholder': '$', 'class': 'form-control'}),
            'contract_type': forms.Select(attrs={'class': 'form-control'}),
            'restaurant_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }        
