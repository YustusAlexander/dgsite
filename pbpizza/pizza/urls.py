from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('customer_account/', get_account, name='customer_account'),
    path('cart/', Cart.as_view(), name='cart'),
    path('check_order/', check_order, name='check_order'),
    path('remove-from-cart/<slug:slug_prod>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('add-to-cart/<slug:slug_prod>/', add_to_cart, name='add-to-cart'),
    path('', home, name='home'),
    path('<int:category_id>/', show_category, name='cat'),
    path('<slug:slug_prod>/', choose_product, name='slug_name_prod'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    # path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)