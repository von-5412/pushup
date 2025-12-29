from django.contrib import admin
from .models import DailyLog, WeeklyMax

@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    list_display = ("date", "total_pushups")
    ordering = ("-date",)

@admin.register(WeeklyMax)
class WeeklyMaxAdmin(admin.ModelAdmin):
    list_display = ("week_start", "max_pushups")
    ordering = ("-week_start",)

