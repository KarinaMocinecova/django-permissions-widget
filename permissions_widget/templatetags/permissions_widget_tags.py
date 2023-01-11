from django import template
try:
    # older Django
    from django.utils.translation import ugettext_lazy as _
except ImportError:
    # Django >= 3
    from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.filter
def get_item(d, key):
    return d.get(key, None)


@register.filter(name='translate')
def translate(text):
    return _(text)
