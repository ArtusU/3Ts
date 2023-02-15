from django.urls import path

from .views import add, team, edit, activate_team, invite


app_name = "team"


urlpatterns = [
    path("add/", add, name="add"),
    path("edit/", edit, name="edit"),
    path("invite/", invite, name="invite"),
    path("<int:team_id>/", team, name="team"),
    path("activate_team/<int:team_id>/", activate_team, name="activate_team"),
]
