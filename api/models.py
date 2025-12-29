from django.db import models
from django.utils import timezone

class DailyLog(models.Model):
    date = models.DateField(default=timezone.localdate, unique=True)
    total_pushups = models.IntegerField(default=0)

    def achievement_level(self):
        if self.total_pushups >= 100:
            return "major"
        if self.total_pushups >= 50:
            return "minor"
        return None

    def __str__(self):
        return f"{self.date} - {self.total_pushups} pushups"


class WeeklyMax(models.Model):
    week_start = models.DateField(unique=True)
    max_pushups = models.IntegerField()

    def __str__(self):
        return f"Week starting {self.week_start} - Max Pushups: {self.max_pushups}"
