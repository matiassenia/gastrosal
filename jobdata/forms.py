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


class JobDataFilterForm(forms.Form):
    POSITION_CHOICES = [
        ('', 'Seleccionar posición'),
        ('Bacherx', 'Bacherx'),
        ('Ayudantx de cocina', 'Ayudantx de cocina'),
        ('Cocinerx', 'Cocinerx'),
        ('Pastelerx', 'Pastelerx'),
        ('Jefx de pastelería', 'Jefx de pastelería'),
        ('Jefx de cocina', 'Jefx de cocina'),
        ('Sommelier', 'Sommelier'),
        ('Camarerx', 'Camarerx'),
        ('Encargadx de sala', 'Encargado de sala'),
        ('Chef ejecutivx', 'Chef ejecutivo'),
        ('Cajerx', 'Cajerx'),
    ]

    CURRENCY_CHOICES = [
        ('', 'Seleccionar moneda'),
        ('USD', 'USD'),
        ('ARS', 'ARS'),
    ]

    CONTRACT_CHOICES = [
        ('', 'Seleccionar tipo de contrato'),
        ('100% en blanco', 'En blanco (Trabajo 100% registrado)'),
        ('100% en negro', 'En negro (Trabajo sin registrar)'),
        ('Media jornada registrada / Media jornada sin registrar', 'Miti-Miti (Media jornada de trabajo registrado, la otra media jornada sin registrar)')
    ]

    position = forms.ChoiceField(choices=POSITION_CHOICES, required=False, label='Posición de Empleo')
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES, required=False, label='Moneda')
    contract_type = forms.ChoiceField(choices=CONTRACT_CHOICES, required=False, label='Tipo de Contrato')