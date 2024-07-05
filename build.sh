#!/bin/bash

# Activar el entorno virtual
source env/bin/activate

# Instalar dependencias
pip3 install -r requirements.txt

# Ejecutar la recopilación de archivos estáticos
python3 manage.py collectstatic --noinput
