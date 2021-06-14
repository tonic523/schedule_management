from django.db import models

from permissions.models.roles import Role
from permissions.models.users_roles import UserRole

class User(models.Model):
    ANNUAL_VACATION = (
        (0, 11),
        (2, 15),
        (3, 16),
        (4, 16),
        (5, 17),
        (6, 17),
        (7, 18),
        (8, 18)
    )
    WORK_TYPE = (
        ('정규', '정규 근무')
        ('시차', '시차출퇴근')
    )
    employee_number     = models.CharField(max_length=64)
    date_of_join        = models.CharField(max_length=64)
    annual_vacation     = models.IntegerField(default=1, choices=ANNUAL_VACATION)
    registration_number = models.CharField(max_length=64)
    roles               = models.ManyToManyField(Role, through=UserRole, related_name='users')
    password            = models.CharField(max_length=128)
    phone_number        = models.CharField(max_length=64)
    email               = models.CharField(max_length=128)
    name                = models.CharField(max_length=100)
    work_type           = models.CharField(max_length=64, default='정규', choices=WORK_TYPE)
    salary              = models.IntegerField()
    get_in_time         = models.TimeField()
    get_off_time        = models.TimeField()

    class Meta:
        db_table = 'users'