from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .models import Details, Skills, Projects
from .forms import SkillsForm, DetailsForm, ProjectsForm



def home(request):
    """
    home page
    """
    context = {
        'title': 'Home'
    }
    return render(request, 'pages/index.html', context)


def about_me(request):
    """
    About me page.
    """
    details = Details.objects.all()
    skills = Skills.objects.all()
    context = {
        'details': details,
        'skills': skills,
        'title': 'About Me'
        }
    return render(request, 'pages/about-me.html', context)


def projects(request):
    """
    Projects page.
    """
    my_projects = Projects.objects.all()
    context = {
        'title': 'My Projects',
        'my_projects': my_projects,
    }
    return render(request, 'pages/projects.html', context)

@staff_member_required
def front_panel(request):
    """
    Front custom admin panel.
    """
    details = Details.objects.all()
    details_form = DetailsForm()
    skills = Skills.objects.all()
    skills_form = SkillsForm()
    my_projects = Projects.objects.all()
    projects_form = ProjectsForm()

    if request.method == 'POST':
        details_form = DetailsForm(request.POST)
        if details_form.is_valid():
            details_form.save()
            messages.success(request, 'Details has been created.')
            return redirect('front_panel')

    if request.method == 'POST':
        skills_form = SkillsForm(request.POST)
        if skills_form.is_valid():
            skills_form.save()
            messages.success(request, 'Skill has been created.')
            return redirect('front_panel')

    if request.method == 'POST':
        projects_form = ProjectsForm(request.POST, request.FILES)
        if projects_form.is_valid():
            projects_form.save()
            messages.success(request, 'Project has been created.')
            return redirect('front_panel')

    context = {
        'details': details,
        'details_form': details_form,
        'skills_form': skills_form,
        'skills': skills,
        'my_projects': my_projects,
        'projects_form': projects_form,
        'title': 'Hello Boss',
        }
    return render(request, 'pages/front-panel.html', context)

@staff_member_required
def edit_skill(request, skill_id):
    """
    Editing skills in front panel.
    """
    skill = get_object_or_404(Skills, id=skill_id)
    if request.method == 'POST':
        skills_form = SkillsForm(request.POST, instance=skill)
        if skills_form.is_valid():
            skills_form.save()
            messages.success(request, 'Skill has been edited.')
            return redirect('front_panel')
    edit_skills_form = SkillsForm(instance=skill)
    context = {
        'edit_skills_form': edit_skills_form,
        'title': 'Lets Edit Boss'
    }

    return render(request, 'pages/edit-skill.html', context)

@staff_member_required
def delete_skill(request, skill_id):
    """
    Deleting skills in front panel.
    """
    skill = get_object_or_404(Skills, id=skill_id)
    skill.delete()
    messages.success(request, 'Skill has been deleted.')
    return redirect('front_panel')

@staff_member_required
def edit_detail(request, detail_id):
    """
    Editing details in front panel.
    """
    detail = get_object_or_404(Details, id=detail_id)
    if request.method == 'POST':
        details_form = DetailsForm(request.POST, instance=detail)
        if details_form.is_valid():
            details_form.save()
            messages.success(request, 'Details has been edited.')
            return redirect('front_panel')
    details_form = DetailsForm(instance=detail)
    context = {
        'details_form': details_form,
        'title': 'Lets Edit Boss'
    }

    return render(request, 'pages/edit-detail.html', context)

@staff_member_required
def delete_detail(request, detail_id):
    """
    Deleting details in front panel.
    """
    detail = get_object_or_404(Details, id=detail_id)
    detail.delete()
    messages.success(request, 'Details has been deleted.')
    return redirect('front_panel')

@staff_member_required
def edit_project(request, project_id):
    """
    Editing projects in front panel.
    """
    project = get_object_or_404(Projects, id=project_id)
    if request.method == 'POST':
        projects_form = ProjectsForm(request.POST,
                                     request.FILES, instance=project)
        if projects_form.is_valid():
            projects_form.save()
            messages.success(request, 'Project has been edited.')
            return redirect('front_panel')
    edit_projects_form = ProjectsForm(instance=project)
    context = {
        'edit_projects_form': edit_projects_form,
        'title': 'Lets Edit Boss'
    }

    return render(request, 'pages/edit-project.html', context)

@staff_member_required
def delete_project(request, project_id):
    """
    Deleting project in front panel.
    """
    project = get_object_or_404(Projects, id=project_id)
    project.delete()
    messages.success(request, 'Project has been deleted.')
    return redirect('front_panel')
