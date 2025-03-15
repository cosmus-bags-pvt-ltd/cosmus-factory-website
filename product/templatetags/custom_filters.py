from django import template
from datetime import datetime

register = template.Library()

@register.filter
def subtract_dates(date1, date2):
    if date1 and date2:

        return (date1 - date2).days  # Returns the difference in days
    return None


@register.filter
def subtract_datestime(date1, date2):
    if date1 and date2:
        date1 = date1.date()
        return (date1 - date2).days  # Returns the difference in days
    return None



@register.filter
def subtract(value, arg):
    """
    Subtracts the arg from the value.
    Usage: {{ value|subtract:arg }}
    """
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return ''


@register.filter
def minus(value, arg):
    """Subtracts arg from value."""
    try:
        return value - arg
    except TypeError:
        return 0
    



