from django.test import TestCase
from django.urls import reverse
from portfolio_app.models import Project

class ProjectModelTest(TestCase):

    def test_create_project(self):
        project = Project.objects.create(
            title="Projeto teste",
            description="Descrição teste",
            link="https://github.com"
        )

        self.assertEqual(project.title, "Projeto teste")


class ViewTest(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello World!")