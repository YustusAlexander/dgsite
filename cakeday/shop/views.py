from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .forms import *
from .models import *
from .utils import *


class CakeHome(DataMixin, ListView):
    model = Cake
    template_name = 'shop/index.html'
    context_object_name = 'posts'
    extra_context = {}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=menu[0]['title'])
        context = dict(list(context.items()) + list(c_def.items()))
        # context['title'] = menu[0]['title']
        return context

    def get_queryset(self):
        return Cake.objects.filter(is_pub=True)

# def index(request):
#     posts = Cake.objects.all()
#     context = {
#         'title': menu[0]['title'],
#         'menu': menu,
#         'posts': posts
#     }
#     return render(request, "shop/index.html", context=context)

def recipes(request):
    posts = Cake.objects.all()
    cats = Category.objects.all()
    context = {
        'title': menu[1]['title'],
        'cats': cats,
        'menu': menu,
        'posts': posts,
        'cat_selected': 0
    }
    return render(request, "shop/recipes.html", context=context)

def about(request):
    context = {
        'title': menu[2]['title'],
        'menu': menu,
        'name_menu': "site_menu",
    }
    return render(request, "shop/about.html", context=context)

# def addpage(request):
#     context = {
#         'title': menu[2]['title']
#     }
#     return render(request, "shop/addpage.html", context=context)

class AddPage(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'shop/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = menu[0]['title']
        context['cat_selected'] = 0
        return context


def login(request):
    context = {
        'title': menu[2]['title']
    }
    return render(request, "shop/login.html", context=context)

# def show_post(request, post_slug):
#     post = get_object_or_404(Cake, slug=post_slug)
#
#     context = {
#         'title': menu[1]['title'],
#         'menu': menu,
#         'post': post,
#         #'cat_selected': 0
#     }
#     return render(request, "shop/post.html", context=context)

class ShowPost(DetailView):
    model = Cake
    template_name = 'shop/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = menu[0]['title']
        context['cat_selected'] = 0
        return context

    # def get_queryset(self):
    #     return Cake.objects.filter(cat__id=self.kwargs['cat_id'], is_pub=True)

def show_category(request, cat_id):
    posts = Cake.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    # if len(posts) == 0:
    #     raise Http484()
    context = {
        'title': menu[1]['title'],
        'cats': cats,
        'menu': menu,
        'posts': posts,
        'cat_selected': cat_id
    }
    return render(request, "shop/recipes.html", context=context)

# class CakeCategory(ListView):
#     model = Cake
#     template_name = 'shop/index.html'
#     context_object_name = 'posts'
#       allow_empty = False
#
#     def get_queryset(self):
#         return Cake.objects.filter(cat__id=self.kwargs['cat_id'], is_pub=True)
#




def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                form.save()
                # Cake.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.aa_error(None, 'Ошибка поста')
    else:
        form = AddPostForm()
    context = {
        'form': form,
        'title': 'add article',
        'menu': menu
    }
    return render(request, "shop/addpage.html", context=context)


# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1>page not found</h1>')


# def categores(request, catid):
#     if (request.GET):
#         print(request.GET)
#     return HttpResponse(f"<h1>Cat.</h1><p>{catid}</p>")
#
# def archive(request, year):
#     return HttpResponse(f"<h1>Cat.</h1><p>{year}</p>")