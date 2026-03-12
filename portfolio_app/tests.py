from django.test import TestCase
from .models import Project

class ProjectModelTest(TestCase):

    def test_create_project(self):
        project = Project.objects.create(
            title="Projeto teste",
            description="Descrição teste",
            link="https://github.com"
        )

        self.assertEqual(project.title, "Projeto teste")