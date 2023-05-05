from django import template
from women.models import *

register = template.Library()


@register.simple_tag(name='get_cats')
def get_categories(filtr=None):
    if not filtr:
        return Category.objects.all()
    return Category.objects.filter(pk=filtr)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=None):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}
