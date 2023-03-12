from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


# class base_template(TemplateView):
#     template_name = 'base.html'
def home(request):
    return render(request, "./index.html")


def aboutMe(request):
    return render(request, "./about-me.html")
