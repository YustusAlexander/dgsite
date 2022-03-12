from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('basket/', basket, name='basket'),
    path('', home, name='home'),
    path('<int:category_id>/', show_category, name='cat'),
    path('<slug:slug_prod>/', choose_product, name='slug_name_prod'),

]

 # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)