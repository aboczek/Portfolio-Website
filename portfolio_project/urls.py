from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutme/', views.about_me, name="about_me"),
    path('projects/', views.projects, name="projects"),
    path('login/', views.login_panel, name="login_panel"),
]
