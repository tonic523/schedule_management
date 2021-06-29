from .users_schedules import urlpatterns as users_schedules_urls
from .login import urlpatterns as login_urls
from .my_page import urlpatterns as my_page_urls
from .me import urlpatterns as me_urls
from .users_employees import urlpatterns as users_employees_urls
from .users_drafts import urlpatterns as users_drafts_urls

app_name = 'schedules'

urlpatterns = [
    # all your other urls
]

urlpatterns += users_schedules_urls
urlpatterns += login_urls
urlpatterns += my_page_urls
urlpatterns += me_urls
urlpatterns += users_employees_urls
urlpatterns += users_drafts_urls
