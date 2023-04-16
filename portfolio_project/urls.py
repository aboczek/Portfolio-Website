from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutme/', views.about_me, name="about_me"),
    path('projects/', views.projects, name="projects"),
    path('front/', views.front_panel, name="front_panel"),
    path('edit-skill/<skill_id>', views.edit_skill, name="edit"),
    path('delete-skill/<skill_id>', views.delete_skill, name='delete'),
    path('edit-detail/<detail_id>', views.edit_detail, name='edit_detail'),
    path('delete-detail/<detail_id>', views.delete_detail, name='delete_detail'),
    path('edit-project/<project_id>', views.edit_project, name='edit_project'),
    path('delete-project/<project_id>', views.delete_project, name='delete_project'),
    path('accounts/', include('allauth.urls')),
]
