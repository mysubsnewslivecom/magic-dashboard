from django import template

register = template.Library()


# @register.filter(name='loglevel')
@register.simple_tag
def log_level(value):
    if value == "success":
        return "bg-success"
    elif value == "error":
        return "bg-danger"
    elif value == "warn":
        return "bg-warning"
    else:
        return "bg-info"
