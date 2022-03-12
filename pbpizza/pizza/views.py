from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages

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
    return render(request, 'pizza/register.html', context=context)

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

def basket(request):
    return render(request, 'pizza/basket.html')

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {'categories': categories, 'products': products, }
    return render(request, 'pizza/index.html', context=context)

def choose_product(request, slug_prod):
    products = get_object_or_404(Product, slug=slug_prod)
    categories = Category.objects.all()
    context = {'categories': categories, 'products': products, }
    return render(request, 'pizza/product.html', context=context)


def show_category(request, category_id):
    categories = Category.objects.all()
    products = Product.objects.filter(category=category_id)
    context = {'categories': categories, 'products': products}
    return render(request, 'pizza/index.html', context=context)




# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1>page not found</h1>')

# menu = [
#         # {'name': 'Пицца', 'url_name': 'pizza'},
#         # {'name': 'Сэндвичи', 'url_name': 'sandwich'},
#         # {'name': 'Дессерты', 'url_name': 'dessert'},
#         # {'name': 'Напитки', 'url_name': 'drink'},
#         # {'name': 'Разное', 'url_name': 'other'},
#         {'name': 'Акции', 'url_name': 'sales'},
#         {'name': 'Статьи', 'url_name': 'articles'}
#         ]