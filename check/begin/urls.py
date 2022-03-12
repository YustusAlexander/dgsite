
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='23'),
    path('<slug:slug_name>', show, name='slug_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
