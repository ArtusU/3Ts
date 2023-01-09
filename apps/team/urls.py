from django.urls import path

from .views import add, team, edit


app_name = "team"


urlpatterns = [
    path("add/", add, name="add"),
    path("edit/", edit, name="edit"),
    path("<int:team_id>/", team, name="team"),
]
