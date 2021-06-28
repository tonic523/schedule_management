from .users_schedules import urlpatterns as users_schedules_urls
from .login import urlpatterns as login_urls
from .my_page import urlpatterns as my_page_urls
from .me import urlpatterns as me_urls
app_name = 'schedules'

urlpatterns = [
    # all your other urls
]

urlpatterns += users_schedules_urls
urlpatterns += login_urls
urlpatterns += my_page_urls
urlpatterns += me_urls