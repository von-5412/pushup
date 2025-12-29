from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_pushups, name="add_pushups"),
    path("weekly/", views.weekly_stats, name="weekly_stats"),
]
