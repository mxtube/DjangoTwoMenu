"""
Navigation
Kirill Kuznetsov 01.05.2023
"""
from django.urls import path
from .views import HomePage, get_category, get_product

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('<str:cat>', get_category, name='category'),
    path('<str:cat>/<str:prod>', get_product, name='product')
]
