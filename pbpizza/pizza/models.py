from django.db import models
from django.urls import reverse_lazy


class Product(models.Model):
    name_product = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    base_price = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Базовая цена')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    components = models.CharField(max_length=255, verbose_name='Состав')
    size = models.CharField(max_length=50, verbose_name='Size')
    photo = models.ImageField(upload_to="photo/", verbose_name='Фото', null=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('slug_name_prod', kwargs={'slug_prod': self.slug})


class Category(models.Model):
    name_category = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse_lazy('cat', kwargs={'category_id': self.pk})

