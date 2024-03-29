# generator/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, css_class):
    """Add CSS class to the given value."""
    return value.as_widget(attrs={'class': css_class})
