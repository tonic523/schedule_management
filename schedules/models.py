from django.db import models
from django.db.models.deletion import CASCADE

class Schedule(models.Model):
    user = models.ForeignKey('users.User', on_delete=CASCADE)
    act = models.ForeignKey('Act', on_delete=CASCADE)
    hours = models.IntegerField(default=0)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    status = models.ForeignKey('ScheduleStatus', on_delete=CASCADE)

    class Meta:
        db_table = 'schedules'

class Act(models.Model):
    name = models.CharField(max_length=64)
    start_at = models.TimeField()

    class Meta:
        db_table = 'acts'

class ScheduleStatus(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'shcedule_status'

