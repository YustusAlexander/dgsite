from django.contrib import admin

# Register your models here.
from .models import *


class CakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'photo', 'time_create', 'time_update', 'is_pub')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_pub',)
    list_filter = ('is_pub', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Cake, CakeAdmin)
admin.site.register(Category, CategoryAdmin)
