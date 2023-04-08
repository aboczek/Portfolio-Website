from django.shortcuts import render, redirect, get_object_or_404
from .models import Details, Skills, Projects
from .forms import SkillsForm, DetailsForm, ProjectsForm

# Create your views here.

def home(request):
    """
    home page
    """
    return render(request, "pages/index.html")


def about_me(request):
    """
    About me page.
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
    Projects page.
    """
    my_projects = Projects.objects.all()
    context = {
        "title": "My Projects",
        "my_projects": my_projects,
    }
    return render(request, "pages/projects.html", context)


def login_panel(request):
    """
    Login panel
    """
    context = {"title": "Login Panel"}
    return render(request, "pages/login.html", context)


def front_panel(request):
    """
    Front custom admin panel.
    """
    if request.method == 'POST':
        skills_form = SkillsForm(request.POST)
        if skills_form.is_valid():
            skills_form.save()
            return redirect('about_me')
    
    if request.method == 'POST':
        projects_form = ProjectsForm(request.POST)
        if projects_form.is_valid():
            projects_form.save()
            return redirect('about_me')

    my_projects = Projects.objects.all()
    projects_form = ProjectsForm()
    details = Details.objects.all()
    skills = Skills.objects.all()
    skills_form = SkillsForm()
    context = {
        "my_projects": my_projects,
        "projects_form": projects_form,
        "skills_form": skills_form,
        "details": details,
        "skills": skills,
        "title": "Hello Boss",
        }
    return render(request, "pages/front-panel.html", context)

def edit_skill(request, skill_id):
    """
    Editing skills in front panel.
    """
    skill = get_object_or_404(Skills, id=skill_id)
    if request.method == 'POST':
        skills_form = SkillsForm(request.POST, instance=skill)
        if skills_form.is_valid():
            skills_form.save()
            return redirect('front_panel')
    edit_form = SkillsForm(instance=skill)
    context = {
        "edit_form": edit_form,
        "title": "Lets Edit Boss"
    }

    return render(request, "pages/edit-skill.html", context)


def delete_skill(request, skill_id):
    """
    Deleting skills in front panel.
    """
    skill = get_object_or_404(Skills, id=skill_id)
    skill.delete()
    return redirect("front_panel")


def edit_detail(request, detail_id):
    """
    Editing details in front panel.
    """
    detail = get_object_or_404(Details, id=detail_id)
    if request.method == 'POST':
        details_form = DetailsForm(request.POST, instance=detail)
        if details_form.is_valid():
            details_form.save()
            return redirect('front_panel')
    details_form = DetailsForm(instance=detail)
    context = {
        "details_form": details_form,
        "title": "Lets Edit Boss"
    }

    return render(request, "pages/edit-detail.html", context)
