from django.urls import path
from . import views

urlpatterns = [
    path('', views.home(), name="home"),
    path('aboutme/', views.aboutMe(), name="about_me"),
    path('projects/', views.projects(), name="projects")
]
