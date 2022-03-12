from django.contrib import admin

# Register your models here.
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post

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


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)