from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Details, Skills, Projects

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
    details = Details.objects.all()
    context = {
        "details": details,
        "title": "test 123"
        }
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


def front_panel(request):
    """
    Front custom admin panel
    """
    context = {"title": "Hello Boss"}
    return render(request, "pages/front-panel.html", context)
