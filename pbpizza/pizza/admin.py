from django.contrib import admin

# Register your models here.
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_product')
    list_display_links = ('id', 'name_product')
    prepopulated_fields = {'slug': ('name_product',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')
    list_display_links = ('id', 'name_category')
    prepopulated_fields = {'slug': ('name_category',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
