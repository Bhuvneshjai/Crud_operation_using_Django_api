from django.http import HttpResponse
from django.shortcuts import redirect, render
from image_handler.models import *


def show_home_page(request):
    images = Image.objects.all()
    category = Category.objects.all()
    data = {'img':images,'cats':category}
    return render(request, "home.html", data)

def show_about_page(request):
    return render(request, "about.html", {})

def show_category_page(request, cid):
    print(cid)
    cats = Category.objects.all()
    cat = Category.objects.get(pk = cid)
    print(cats)
    images = Image.objects.filter(catgry = cat)
    data = {'img':images, 'cats':cats}
    return render(request, "home.html", data)

def home(request):
    return redirect('/home')
