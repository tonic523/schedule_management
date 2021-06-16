from .schedules import urlpatterns as schedules_urls

app_name = 'schedules'

urlpatterns = [
    # all your other urls
]

urlpatterns += schedules_urls