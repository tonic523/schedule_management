from django.urls import path

from schedules.views import schedules

urlpatterns = [
    path('', schedules.as_view())
]