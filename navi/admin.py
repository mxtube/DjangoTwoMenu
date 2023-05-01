from django.contrib import admin
from .models import MenuCategory, MenuChildren

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'url': ('name',)}

@admin.register(MenuChildren)
class MenuCategoryChildrenAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'url': ('name',)}