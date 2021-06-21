from django.urls import path

from users.views.users_schedules import UserSchedule

urlpatterns = [
    path('/<str:employee_number>/schedules', UserSchedule.as_view())
]