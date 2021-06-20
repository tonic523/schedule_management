from django.urls import path

from users.views.login import login

urlpatterns = [
    path('/login', login)
]