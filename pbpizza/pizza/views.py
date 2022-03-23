from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.views import View
from django.contrib import messages
from django.views.generic import ListView

from .forms import UserRegisterForm, UserLoginForm, CouponForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.conf import settings
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегистрированы")
            return redirect('home')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'pizza/register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'pizza/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    categories = Category.objects.all()
    products = Item.objects.all()
    context = {'categories': categories, 'products': products, }
    return render(request, 'pizza/index.html', context)

def choose_product(request, slug_prod):
    products = get_object_or_404(Item, slug=slug_prod)
    categories = Category.objects.all()
    context = {'categories': categories, 'products': products, }
    return render(request, 'pizza/product.html', context)


def show_category(request, category_id):
    categories = Category.objects.all()
    products = Item.objects.filter(category=category_id)
    context = {'categories': categories, 'products': products}
    return render(request, 'pizza/index.html', context)


def get_account(request):
    orders = Order.objects.filter(user=request.user).order_by('-ordered_date')
    # order_items = orders.filter(items=OrderItem.id)
    context = {'orders': orders,} # 'order_items': order_items}
    return render(request, 'pizza/account.html', context)





class Cart(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'order': order,
            }
            return render(self.request, 'pizza/cart.html', context)
        except ObjectDoesNotExist:
            messages.info(self.request, "cart empty")
            return redirect("/")


@login_required
def add_to_cart(request, slug_prod):
    item = get_object_or_404(Item, slug=slug_prod)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,  user=request.user,  ordered=False )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.success(request, "+1")
        else:
            order.items.add(order_item)
            messages.success(request, "add item")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.success(request, "create order, add item")
    return redirect('cart')

@login_required
def remove_from_cart(request, slug_prod):
    item = get_object_or_404(Item, slug=slug_prod)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, 'quantity updated')

        else:

            messages.info(request, 'quantity updated')

    else:
        messages.info(request, 'quantity updated')
    return redirect('cart')

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")

        else:
            messages.info(request, "This item was not in your cart")

    else:
        messages.info(request, "You do not have an active order")
    return redirect('cart')

@login_required
def check_order(request):
    order = Order.objects.get(user=request.user, ordered=False)
    try:
        # order_items = OrderItem.objects.get(user=request.user, ordered=False)
        order_items = order.items.all()
        order_items.update(ordered=True)
        for item in order_items:
            item.save()
        order.ordered = True
        order.save()
        messages.success(request, "Your order was successful!")
    except:
        messages.warning(request, "Invalid data received")
    return redirect('home')


class AddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(
                    user=self.request.user, ordered=False)
                order.coupon = get_coupon(self.request, code)
                order.save()
                messages.success(self.request, "Successfully added coupon")
                return redirect("core:checkout")
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect("core:checkout")

def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(request, "This coupon does not exist")
        return redirect("core:checkout")