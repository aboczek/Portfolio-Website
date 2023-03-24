from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    """
    home page
    """
    return render(request, "pages/index.html")


def about_me(request):
    """
    About me page
    """
    context = {"title": "test 123"}
    return render(request, "pages/about-me.html", context)


def projects(request):
    """
    Projects page
    """
    context = {"title": "my Projects"}
    return render(request, "pages/projects.html", context)

def login_panel(request):
    """
    Login panel
    """
    context = {"title": "Login Panel"}
    return render(request, "pages/login.html", context)
