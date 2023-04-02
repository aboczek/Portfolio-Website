from django.shortcuts import render, redirect
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
    skills = Skills.objects.all()
    context = {
        "details": details,
        "skills": skills,
        "title": "About Me"
        }
    return render(request, "pages/about-me.html", context)


def projects(request):
    """
    Projects page
    """
    context = {"title": "My Projects"}
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
    if request.method == 'POST':
        skill = request.POST.get('front_skill')
        Skills.objects.create(skill=skill)

        return redirect('about_me')
    context = {"title": "Hello Boss"}
    return render(request, "pages/front-panel.html", context)
