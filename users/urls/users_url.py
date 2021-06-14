from django.urls import include, path

from users.views.users_view import ListUsers

urlpatterns = [
    path('', ListUsers.as_view()),
]