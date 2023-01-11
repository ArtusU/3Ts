from django.urls import path

from .views import projects, project

app_name = "project"

urlpatterns = [
    path("", projects, name="projects"),
    path('<int:project_id>/', project, name='project'),
]
