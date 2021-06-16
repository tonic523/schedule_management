from django.urls import path, include

urlpatterns = [
    path('schedules', include('schedules.urls')),
    path('users', include('users.urls'))
]