from django.db import models

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)

from permissions.models.roles       import Role
from permissions.models.users_roles import UserRole

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name,  date_of_join, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email        = self.normalize_email(email),
            name         = name,
            date_of_join = date_of_join
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
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
        ('정규', '정규 근무'),
        ('시차', '시차출퇴근')
    )
    employee_number     = models.CharField(max_length=64)
    date_of_join        = models.CharField(max_length=64)
    annual_vacation     = models.IntegerField(default=1, choices=ANNUAL_VACATION)
    registration_number = models.CharField(max_length=64)
    roles               = models.ManyToManyField(Role, through=UserRole, related_name='users')
    phone_number        = models.CharField(max_length=64)
    email               = models.CharField(max_length=128, unique=True)
    name                = models.CharField(max_length=100)
    work_type           = models.CharField(max_length=64, default='정규', choices=WORK_TYPE)
    salary              = models.IntegerField()
    get_in_time         = models.TimeField()
    get_off_time        = models.TimeField()

    class Meta:
        db_table = 'users'
    
    objects = CustomUserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['name']