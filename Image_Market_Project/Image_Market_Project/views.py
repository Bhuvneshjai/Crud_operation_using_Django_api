from django.http import HttpResponse
from django.shortcuts import redirect, render


def show_home_page(request):
    return render(request, "home.html", {})

def show_about_page(request):
    return render(request, "about.html", {})

