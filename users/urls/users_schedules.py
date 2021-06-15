from django.urls import path

from users.views.users_schedules import today_user_schedule, commute_record

urlpatterns = [
    path('', today_user_schedule),
    path('/<int:id>/schedules', commute_record)
]