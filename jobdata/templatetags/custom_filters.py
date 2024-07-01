from django import template

register = template.Library()

@register.filter(name='currency_format')
def currency_format(value):
    try:
        # Formatear el valor como string usando puntos como separadores de miles
        return "{:,.0f}".format(value).replace(",", ".")
    except ValueError:
        return value