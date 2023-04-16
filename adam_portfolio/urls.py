"""adam_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio_project import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('aboutme/', views.about_me, name="about_me"),
    path('projects/', views.projects, name="projects"),
    path('front/', views.front_panel, name="front_panel"),
    path('edit-skill/<skill_id>', views.edit_skill, name='edit'),
    path('delete-skill/<skill_id>', views.delete_skill, name='delete'),
    path('edit-detail/<detail_id>', views.edit_detail, name='edit_detail'),
    path('delete-detail/<detail_id>', views.delete_detail, name='delete_detail'),
    path('edit-project/<project_id>', views.edit_project, name='edit_project'),
    path('delete-project/<project_id>', views.delete_project, name='delete_project'),
    path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
