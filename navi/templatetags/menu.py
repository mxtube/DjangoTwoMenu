from django import template
from navi.models import MenuCategory

register = template.Library()

@register.inclusion_tag('mainmenu_tpl.html')
def show_menu(menu_class='menu', active=''):
    categories = MenuCategory.objects.all()
    return {
        "categories": categories,
        "menu_class": menu_class,
        "active_menu": f'{active}'
    }