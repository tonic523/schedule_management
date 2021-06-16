from .users_schedules import urlpatterns as users_schedules_urls

app_name = 'schedules'

urlpatterns = [
    # all your other urls
]

urlpatterns += users_schedules_urls