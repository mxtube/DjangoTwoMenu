from django.db import models
from django.urls import reverse

class MenuCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text='Укажите наименование категории (пример: \'О Нас\')',
        verbose_name='Наименование категории'
    )
    url = models.CharField(
        max_length=255,
        default='',
        help_text='Укажите путь к странице без слэша (пример: \'product\')',
        verbose_name='Путь'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return '%s' % (self.name)

    def get_children(self):
        return MenuChildren.objects.filter(parent=self.pk)

    def get_absolute_url(self):
        return reverse('category', kwargs={"cat": self.url })

class MenuChildren(models.Model):
    parent = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, verbose_name='Родительская категория')
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=255, default='')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return '%s' % (self.name)

    def get_absolute_url(self):
        return reverse('product', kwargs={ "cat": self.parent.url, "prod": self.url })