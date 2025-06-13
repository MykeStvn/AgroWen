from django import template

register = template.Library()

@register.filter
def filter(perfiles, usuario):
    try:
        return perfiles.get(user=usuario)
    except:
        return None 
        