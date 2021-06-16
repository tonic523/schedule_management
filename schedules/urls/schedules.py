from django.urls import path

from schedules.views import scheduleList

urlpatterns = [
    path('', scheduleList)
]