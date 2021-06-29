from django.urls import path

from users.views.users_employees import UserEmployee

urlpatterns = [
    path('/<str:employee_number>/employees', UserEmployee.as_view())
]