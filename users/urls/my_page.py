from django.urls import path

from users.views.my_page import MyPage

urlpatterns = [
    path('/mypage', MyPage.as_view())
]