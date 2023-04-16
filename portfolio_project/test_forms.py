from django.test import TestCase
from .forms import SkillsForm, DetailsForm, ProjectsForm

class TestSkillsForm(TestCase):
    """
    Test Case for forms.
    """
    def test_skill_is_required(self):
        """
        Testing if skill are required.
        """
        form = SkillsForm({'skill': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('skill', form.errors.keys())
        self.assertEqual(form.errors['skill'][0], 'This field is required.')

    def test_detail_is_required(self):
        """
        Testing if detail is required.
        """
        form = DetailsForm({'full_name': '',
                            'age': '',
                            'nationality': '',
                            'languages': '',
                            'address': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertIn('age', form.errors.keys())
        self.assertIn('nationality', form.errors.keys())
        self.assertIn('languages', form.errors.keys())
        self.assertIn('address', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')
        self.assertEqual(form.errors['age'][0], 'This field is required.')
        self.assertEqual(form.errors['nationality'][0], 'This field is required.')
        self.assertEqual(form.errors['languages'][0], 'This field is required.')
        self.assertEqual(form.errors['address'][0], 'This field is required.')

    def test_project_is_required(self):
        """
        Testing if fields in project are required except image which can be placeholder.
        """
        form = ProjectsForm({'title': '',
                             'project_link': '',
                             'project_description': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertIn('project_link', form.errors.keys())
        self.assertIn('project_description', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
        self.assertEqual(form.errors['project_link'][0], 'This field is required.')
        self.assertEqual(form.errors['project_description'][0], 'This field is required.')

    def test_project_image_is_placeholder(self):
        """
        Testing if image has placeholder.
        """
        form = ProjectsForm({'project_image': 'placeholder'})
        self.assertTrue(form.is_valid)
        