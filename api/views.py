from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import DailyLog, WeeklyMax

def home(request):
    today = timezone.localdate()
    daily_log, _ = DailyLog.objects.get_or_create(date=today)

    week_start = today - timedelta(days=today.weekday())

    weekly_max = WeeklyMax.objects.filter(
        week_start=week_start
    ).first()

    context = {
        "daily_log": daily_log,
        "achievement": daily_log.achievement_level(),
        "weekly_max": weekly_max,  # may be None
    }

    return render(request, "home.html", context)

def edit_weekly_max(request):
    today = timezone.localdate()
    week_start = today - timedelta(days=today.weekday())

    week, _ = WeeklyMax.objects.get_or_create(
        week_start=week_start,
        defaults={"max_pushups": 0}
    )

    if request.method == "POST":
        week.max_pushups = int(request.POST.get("max_pushups"))
        week.save()
        return redirect("weekly_stats")

    return render(request, "edit_weekly.html", {"week": week})

def weekly_stats(request):
    weeks = WeeklyMax.objects.order_by("-week_start")
    return render(request, "weekly.html", {"weeks": weeks})



def add_pushups(request):
    if request.method == "POST":
        pushups = int(request.POST.get("pushups", 0))
        today = timezone.localdate()

        daily_log, _ = DailyLog.objects.get_or_create(date=today)
        daily_log.total_pushups += pushups
        daily_log.save()

    return redirect("home")
