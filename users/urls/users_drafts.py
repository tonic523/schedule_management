from django.urls import path

from users.views.users_drafts import UserDraft

urlpatterns = [
    path('/<str:employee_number>/drafts', UserDraft.as_view())
]