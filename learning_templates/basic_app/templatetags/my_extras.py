from django import relative_url_templates

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts our all values of "arg" from the string.
    """
    return value.replace(arg, '')

#register.filter('cut',cut)
