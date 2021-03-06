from django.db import models
from b2tech_intern_20.settings import AUTH_USER_MODEL
class Schedule(models.Model):
    TYPE = (
        ('유급휴가', 8),
        ('무급휴가', 0),
        ('정상근무', 8),
    )
    user       = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    work_type  = models.CharField(max_length=64, choices=TYPE, default='정상근무')
    created_at = models.DateTimeField(null=True, default=None)
    updated_at = models.DateTimeField(null=True, default=None)
    get_in_time = models.TimeField(null=True, default=None)
    get_off_time = models.TimeField(null=True, default=None)

    class Meta:
        db_table = 'schedules'
        app_label = 'schedules'