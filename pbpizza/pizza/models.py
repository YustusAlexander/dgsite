from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.db import models




class Item(models.Model):
    name_product = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    base_price = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Базовая цена')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    components = models.CharField(max_length=255, verbose_name='Состав')
    photo = models.ImageField(upload_to="photo/", verbose_name='Фото', null=True, blank=True)
    def __str__(self):
        return self.name_product
    def get_absolute_url(self):
        return reverse_lazy('slug_name_prod', kwargs={'slug_prod': self.slug})
    def get_add_to_cart_url(self):
        return reverse_lazy('add-to-cart', kwargs={'slug_prod': self.slug})
    def get_remove_from_cart_url(self):
        return reverse_lazy('remove-from-cart', kwargs={'slug_prod': self.slug})

class Category(models.Model):
    name_category = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    def __str__(self):
        return self.name_category
    def get_absolute_url(self):
        return reverse_lazy('cat', kwargs={'category_id': self.pk})

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    @property
    def get_total(self):
        total = self.item.base_price * self.quantity
        return total

status_choises = (('W', 'waited'), ('A', 'accepted'), ('S', 'start'), ('F', 'finish'))
delivery_choises = (('S', 'self'), ('D', 'deliveryman'))

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=status_choises, max_length=1)
    delivery = models.CharField(choices=delivery_choises, max_length=1)
    comment = models.CharField(max_length=255, null=True, blank=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        order_items = self.items.all()
        total = sum([item.get_total for item in order_items])
        return total
    @property
    def get_cart_items(self):
        order_items = self.items.all()
        total = sum([item.quantity for item in order_items])
        return total

    @property
    def get_check_order_url(self):
        return reverse_lazy('check_order')

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()
    def __str__(self):
        return self.code


##########################

class Post(models.Model):
    pass