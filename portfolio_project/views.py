from django.shortcuts import render, redirect, get_object_or_404
from .models import Details, Skills, Projects
from .forms import SkillsForm

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
        skills_form = SkillsForm(request.POST)
        if skills_form.is_valid():
            skills_form.save()
            return redirect('about_me')


    details = Details.objects.all()
    skills = Skills.objects.all()
    skills_form = SkillsForm()
    context = {
        "skills_form": skills_form,
        "title": "Hello Boss",
        "details": details,
        "skills": skills
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
            return redirect('about_me')
    edit_form = SkillsForm(instance=skill)
    context = {
        "edit_form": edit_form,
        "title": "Lets Edit Boss"
    }

    return render(request, "pages/edit-skill.html", context)
