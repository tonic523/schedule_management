from .users_schedules import urlpatterns as users_schedules_urls
from .login import urlpatterns as login_urls
app_name = 'schedules'

urlpatterns = [
    # all your other urls
]

urlpatterns += users_schedules_urls
urlpatterns += login_urls