from django.db import models
from django.core.validators import MinValueValidator 

class JobData(models.Model):
    POSITION_CHOICES = [
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
        ('USD', 'USD'),
        ('ARS', 'ARS'),
    ]
    
    CONTRACT_CHOICES = [
        ('100% en blanco', 'En blanco(Trabajo 100% registrado)'),
        ('100% en negro', 'En negro(Trabajo sin registrar)'),
        ('Media jornada registrada / Media jornada sin registrar', 'Media jornada de trabajo registrado, la otra media jornada sin registrar')
    ]
    
    GENDER_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    ]
    
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=0, validators=[MinValueValidator(1)])
    contract_type = models.CharField(max_length=100, choices=CONTRACT_CHOICES)
    restaurant_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    
    def __str__(self):
        return f'{self.position} - ${self.salary} {self.currency}'
