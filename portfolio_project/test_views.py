from django.test import TestCase
from .models import Details, Skills, Projects

class TestViews(TestCase):
    """
    Testing views for portfolio project.
    """
    def test_get_home(self):
        """
        Test if home is up and running.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')

    def test_get_about_me(self):
        """
        Test if about me is up and running.
        """
        response = self.client.get('/aboutme/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about-me.html')

    def test_get_projects(self):
        """
        Test if projects is up and running.
        """
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/projects.html')

    def test_get_front_panel(self):
        """
        Test if front panel is up and running.
        """
        response = self.client.get('/front/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/front-panel.html')

    def test_get_edit_details(self):
        """
        Test if edit details is up and running.
        """
        detail = Details.objects.create(full_name='Test',
                                        age='900',
                                        nationality='poland',
                                        languages='polish',
                                        address='ireland')
        response = self.client.get(f'/edit-detail/{detail.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/edit-detail.html')

    def test_get_edit_skills(self):
        """
        Test if edit skills is up and running.
        """
        skill = Skills.objects.create(skill='skills')
        response = self.client.get(f'/edit-skill/{skill.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/edit-skill.html')

    def test_get_edit_projects(self):
        """
        Test if edit projects is up and running.
        """
        project = Projects.objects.create(title='test',
                                          project_link='https://www.google.com/',
                                          project_description='testing',
                                          project_image='placeholder')
        response = self.client.get(f'/edit-project/{project.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/edit-project.html')

    def test_can_add_details(self):
        """
        Test if add details is working.
        """
        response = self.client.post('/front/',
                                   {'full_name':'Test',
                                    'age': '900',
                                    'nationality': 'poland', 
                                    'languages': 'polish', 
                                    'address': 'ireland'})
        self.assertRedirects(response, '/front/')

    def test_can_delete_details(self):
        """
        Test if delete details is working.
        """
        detail = Details.objects.create(full_name='Test',
                                        age='900',
                                        nationality='poland',
                                        languages='polish',
                                        address='ireland')
        response = self.client.get(f'/delete-detail/{detail.id}')
        self.assertRedirects(response, '/front/')
        existing_details = Details.objects.filter(id=detail.id)
        self.assertEqual(len(existing_details), 0)

    def test_can_add_skills(self):
        """
        Test if add skills is working.
        """
        response = self.client.post('/front/', {'skill': 'Testing skills'})
        self.assertRedirects(response, '/front/')

    def test_can_delete_skills(self):
        """
        Test if delete skills is working.
        """
        skill = Skills.objects.create(skill='Test skills')
        response = self.client.get(f'/delete-skill/{skill.id}')
        self.assertRedirects(response, '/front/')
        existing_skills = Skills.objects.filter(id=skill.id)
        self.assertEqual(len(existing_skills), 0)

    def test_can_add_projects(self):
        """
        Test if add projects is working.
        """
        response = self.client.post('/front/', {'title': 'test',
                                                'project_link': 'https://www.google.com/',
                                                'project_description': 'testing',
                                                'project_image': 'placeholder'})
        self.assertRedirects(response, '/front/')

    def test_can_delete_projects(self):
        """
        Test if can delete projects is working.
        """
        project = Projects.objects.create(title='test',
                                          project_link='https://www.google.com/',
                                          project_description='testing',
                                          project_image='placeholder')
        response = self.client.get(f'/delete-project/{project.id}')
        self.assertRedirects(response, '/front/')
        existing_projects = Projects.objects.filter(id=project.id)
        self.assertEqual(len(existing_projects), 0)

    def test_can_edit_details(self):
        """
        Test if can edit details is working.
        """
        detail = Details.objects.create(full_name='Test',
                                        age='900',
                                        nationality='poland',
                                        languages='polish',
                                        address='ireland')
        response = self.client.post(f'/edit-detail/{detail.id}', {'full_name': 'Test edit',
                                                                  'age': '900',
                                                                  'nationality': 'poland',
                                                                  'languages': 'polish',
                                                                  'address': 'ireland'})
        self.assertRedirects(response, '/front/')
        updated_detail = Details.objects.get(id=detail.id)
        self.assertEqual(updated_detail.full_name, 'Test edit')

    def test_can_edit_skills(self):
        """
        Test if can edit skills is working.
        """
        skill = Skills.objects.create(skill='Test')
        response = self.client.post(f'/edit-skill/{skill.id}', {'skill': 'Test edit'})
        self.assertRedirects(response, '/front/')
        updated_skill = Skills.objects.get(id=skill.id)
        self.assertEqual(updated_skill.skill, 'Test edit')

    def test_can_edit_project(self):
        """
        Test if can edit projects is working.
        """
        project = Projects.objects.create(title='test',
                                          project_link='https://www.google.com/',
                                          project_description='testing',
                                          project_image='placeholder')
        response = self.client.post(f'/edit-project/{project.id}',
                                                    {'title': 'Title edit',
                                                     'project_link': 'https://www.google.com/',
                                                     'project_description': 'testing',
                                                     'project_image': 'placeholder'})
        self.assertRedirects(response, '/front/')
        updated_project = Projects.objects.get(id=project.id)
        self.assertEqual(updated_project.title, 'Title edit')
        