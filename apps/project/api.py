from datetime import datetime, timezone
from django.http import JsonResponse
from .models import Entry


def api_start_timer(request):
    entry = Entry.objects.create(
        team_id=request.user.userprofile.active_team_id,
        minutes=0,
        created_by=request.user,
        is_tracked=False,
        created_at=datetime.now(),
    )
    return JsonResponse({"success": True})


def api_stop_timer(request):
    entry = Entry.objects.get(
        team_id=request.user.userprofile.active_team_id,
        created_by=request.user,
        minutes=0,
        is_tracked=False,
    )
    tracked_minutes = int(
        (datetime.now(timezone.utc) - entry.created_at).total_seconds() / 60
    )
    if tracked_minutes < 1:
        tracked_minutes = 1
    entry.minutes = tracked_minutes
    entry.is_tracked = False
    entry.save()
    return JsonResponse({"success": True, "entryID": entry.id})


def api_discard_timer(request):
    entries = Entry.objects.filter(
        team_id=request.user.userprofile.active_team_id,
        created_by=request.user,
        is_tracked=False,
    ).order_by("-created_at")
    if entries:
        entry = entries.first()
        entry.delete()
    return JsonResponse({"success": True})