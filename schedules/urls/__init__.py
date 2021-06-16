from .schedules import urlpatterns as schedules_urls
from .schedules_today import urlpatterns as schedule_today_urls
app_name = 'schedules'

urlpatterns = [
    # all your other urls
]

urlpatterns += schedules_urls
urlpatterns += schedule_today_urls