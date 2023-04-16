from django.test import TestCase
from .models import Details, Skills, Projects

class TestModels(TestCase):
    """
    Testing models
    """
    def test_details_model(self):
        """
        Testing details model.
        """
        detail = Details.objects.create(full_name='Test Name',
                                        age='900',
                                        nationality='poland',
                                        languages='polish',
                                        address='poland')
        self.assertEqual(detail.full_name, 'Test Name')
        self.assertEqual(detail.age, '900')
        self.assertEqual(detail.nationality, 'poland')
        self.assertEqual(detail.languages, 'polish')
        self.assertEqual(detail.address, 'poland')

    def test_skills_model(self):
        """
        Testing skills model.
        """
        skill = Skills.objects.create(skill='Testing skill')
        self.assertEqual(skill.skill, 'Testing skill')

    def test_projects_model(self):
        """
        Testing projects model.
        """
        project = Projects.objects.create(title='Testing title',
                                          project_link='https://github.com/',
                                          project_description='Test description',
                                          project_image='placeholder')
        self.assertEqual(project.title, 'Testing title')
        self.assertEqual(project.project_link, 'https://github.com/')
        self.assertEqual(project.project_description, 'Test description')
        self.assertEqual(project.project_image, 'placeholder')

    def test_details_string_method_returns_name(self):
        """
        Testing string method in details.
        """
        detail = Details.objects.create(full_name='Test Name',
                                        age='900',
                                        nationality='poland',
                                        languages='polish',
                                        address='poland')
        self.assertEqual(str(detail), 'Test Name')

    def test_skills_string_method_returns_name(self):
        """
        Testing string method in skills.
        """
        skill = Skills.objects.create(skill='Testing skill')
        self.assertEqual(str(skill), 'Testing skill')

    def test_projects_string_method_returns_name(self):
        """
        Testing string method in projects
        """
        project = Projects.objects.create(title='Testing title',
                                          project_link='https://github.com/',
                                          project_description='Test description',
                                          project_image='placeholder')
        self.assertEqual(str(project), 'Testing title')
