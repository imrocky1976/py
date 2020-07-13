from django import template

register = template.Library()

def replace(value, arg):
    "Replace all values of arg to _ from the giving string"
    return value.replace(arg, "_")

@register.filter(name='lower')
def lower(value):
    "Converts a string into all lowercase"
    return value.lower()

register.filter('replace', replace)