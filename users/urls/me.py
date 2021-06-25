from django.urls import path

from users.views.me import Me

urlpatterns = [
    path('/me', Me.as_view())
]