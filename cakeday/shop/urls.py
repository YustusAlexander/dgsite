from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', CakeHome.as_view(), name="home"),
    # path('', index, name="home"),
    path('recipes', recipes, name="recipes"),
    path('about', about, name="about"),
    # path('addpage', addpage, name="addpage"),
    path('addpage', AddPage.as_view(), name="addpage"),
    path('login', login, name="login"),
    # path('post/<slug:post_slug>/', show_post, name="post"),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name="post"),
    path('category/<int:cat_id>/', show_category, name="category"),
    # path('category/<int:cat_id>/', CakeCategory, name="category")

    # path('cats/<int:catid>', categores),  # http://127.0.0.1:8000/cats/
    # re_path(r"^archive/(?P<year>[0-9]{4})/", archive)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)