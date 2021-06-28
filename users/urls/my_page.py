from django.urls import path

from users.views.my_page import MyPage

urlpatterns = [
    path('/<str:employee_number>/mypage', MyPage.as_view())
]