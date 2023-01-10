from django.urls import path

from .views import projects

app_name = "project"

urlpatterns = [
    path("", projects, name="projects"),
]
