from django import template


def format_minutes(value):
    return "{:2d}h {:2d}min".format(*divmod(value, 60))


register = template.Library()
register.filter("format_minutes", format_minutes)
