from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from apps.project.models import Entry
from apps.team.models import Team

from .utilities import (
    get_time_for_user_and_date,
    get_time_for_team_and_month,
    get_time_for_user_and_month,
    get_time_for_user_and_project_and_month,
    get_time_for_user_and_team_month,
)


@login_required
def dashboard(request):
    if not request.user.userprofile.active_team_id:
        return redirect("myaccount")

    team = get_object_or_404(
        Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE
    )
    all_projects = team.projects.all()
    members = team.members.all()

    num_days = int(request.GET.get("num_days", 0))
    date_user = datetime.now() - timedelta(days=num_days)

    date_entries = Entry.objects.filter(
        team=team, created_by=request.user, created_at__date=date_user, is_tracked=True
    )

    user_num_months = int(request.GET.get("user_num_months", 0))
    user_month = datetime.now() - relativedelta(months=user_num_months)

    for project in all_projects:
        project.time_for_user_and_project_and_month = (
            get_time_for_user_and_project_and_month(
                team, project, request.user, user_month
            )
        )

    context = {
        "team": team,
        "all_projects": all_projects,
        "projects": all_projects[0:4],
        "members": members,
        "num_days": num_days,
        "user_num_months": user_num_months,
        "user_month": user_month,
        "date_user": date_user,
        "date_entries": date_entries,
        "time_for_user_and_month": get_time_for_user_and_month(
            team, request.user, user_month
        ),
        "time_for_user_and_date": get_time_for_user_and_date(
            team, request.user, date_user
        ),
    }

    return render(request, "dashboard/dashboard.html", context)
