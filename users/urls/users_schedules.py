from django.urls import path

from users.views.users_schedules import record_commute

urlpatterns = [
    path('/<str:employee_number>/schedules', record_commute)
]