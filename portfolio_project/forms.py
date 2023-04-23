from django import forms
from .models import Details, Skills, Projects


class SkillsForm(forms.ModelForm):
    """
    Skills form.
    """
    class Meta:
        """
        Meta for skills form.
        """
        model = Skills
        fields = ['skill', ]


class DetailsForm(forms.ModelForm):
    """
    Details form.
    """
    class Meta:
        """
        Meta for details form.
        """
        model = Details
        fields = ['full_name', 'age', 'nationality', 'languages', 'address']


class ProjectsForm(forms.ModelForm):
    """
    Projects Form.
    """
    class Meta:
        """
        Meta for details form.
        """
        model = Projects
        fields = ['title', 'project_link',
                  'project_description', 'project_image']
