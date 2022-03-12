from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import *

def index(request):
    mod = Begin.objects.all()
    context = {
        'mod': mod,
        'name': 'v',
    }
    return render(request, 'begin/index.html', context=context)

# def index(request):
#     return HttpResponse("12312")


def show(request, slug_name):
    db = get_object_or_404(Begin, slug=slug_name)
    context = {
        'title': db.title
    }
    return render(request, 'begin/show.html', context=context)
