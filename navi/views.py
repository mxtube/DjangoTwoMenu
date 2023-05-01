from django.shortcuts import render
from django.views import View
from .models import MenuCategory, MenuChildren

class HomePage(View):
    template_path = 'index.html'

    def get(self, request, *args, **kwargs):
        context = { 'title': 'Главная страница', }
        return render(request, template_name=self.template_path, context=context)

def get_category(request, cat):
    category = MenuCategory.objects.get(url=cat)
    context = { 'title': category.name, }
    return render(request, template_name='category.html', context=context)

def get_product(request, cat, prod):
    product = MenuChildren.objects.get(parent__url=cat, url=prod)
    context = { 'title': product.name, }
    return render(request, template_name='product.html', context=context)