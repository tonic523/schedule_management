from django.urls import path

from schedules.views import today_schedule

urlpatterns = [
    path('/today', today_schedule)
]