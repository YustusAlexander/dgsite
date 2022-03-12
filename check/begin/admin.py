from django.contrib import admin

# Register your models here.
from .models import *


class BeginAdmin(admin.ModelAdmin):
    list_filter = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Begin, BeginAdmin)