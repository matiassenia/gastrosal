#!/bin/bash

# Activar el entorno virtual
source env/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la recopilación de archivos estáticos
python manage.py collectstatic --noinput

