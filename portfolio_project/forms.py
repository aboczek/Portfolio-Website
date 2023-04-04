from django import forms
from .models import Details, Skills, Projects


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill',]
