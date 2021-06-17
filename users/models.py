from django.db import models

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name,  date_of_join, password=None):
        if not email:
            raise ValueError("이메일 입력해주세요")

        user = self.model(
            email        = self.normalize_email(email),
            name         = name,
            date_of_join = date_of_join
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    WORK_TYPE = (
        ('정규', '정규 근무'),
        ('시차', '시차출퇴근')
    )

    DEFAULT_SALARY = 1822480
    
    employee_number     = models.CharField(max_length=64)
    date_of_join        = models.DateField(max_length=64)
    annual_leave     = models.ForeignKey('users.AnnualLeave', on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=64)
    phone_number        = models.CharField(max_length=64)
    email               = models.CharField(max_length=128, unique=True)
    name                = models.CharField(max_length=100)
    work_type           = models.CharField(max_length=64, default='정규', choices=WORK_TYPE)
    salary              = models.IntegerField(default=DEFAULT_SALARY)
    get_in_time         = models.TimeField(default='09:00')
    get_off_time        = models.TimeField(default='18:00')
    remaining_annual_leave = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = 'users'
        app_label = 'users'
    
    objects = CustomUserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['name']

class AnnualLeave(models.Model):
    annual = models.IntegerField()
    leave_count = models.IntegerField()

    class Meta:
        db_table = 'annual_leaves'