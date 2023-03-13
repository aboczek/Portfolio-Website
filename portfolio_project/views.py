from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


# Home page
def home(request):
    return render(request, "./index.html")


# About me page
def aboutMe(request):
    return render(request, "./about-me.html")


# Projects page
def projects(request):
    return render(request, "./projects.html")