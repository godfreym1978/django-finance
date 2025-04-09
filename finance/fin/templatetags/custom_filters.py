# fin/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def custom_getattr(obj, attr_name):
    return getattr(obj, attr_name, '')