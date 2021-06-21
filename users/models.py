from django.db import models

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)

from users.utils import encrypt_utils

class CustomUserManager(BaseUserManager):
    def create_user(self, email, registration_number, date_of_join, annual=0, **kwargs):
        # phone_number,  name
        REQUIRED_FIELD = (
            'phone_number', 'name', 'work_type', 'salary', 'get_in_time', 'get_off_time', 'remaining_annual_leave'
        )

        if not email:
            raise ValueError("이메일 입력해주세요")

        if not registration_number:
            raise ValueError("주민등록번호 입력해주세요")

        if not date_of_join:
            raise ValueError("입사일 입력해주세요")

        for key in kwargs.keys():
            if key not in REQUIRED_FIELD:
                raise KeyError("key 값을 확인해주세요")

        annual_leave = AnnualLeave.objects.get(annual = annual)
        user = self.model(
            email = self.normalize_email(email),
            annual_leave = annual_leave,
            date_of_join = date_of_join,
            **kwargs
        )
        user.save(using=self._db)
        user.employee_number = date_of_join.split('-')[0] + str(user.id).zfill(4)
        user.set_password(registration_number.split('-')[1])
        user.registration_number = encrypt_utils.encryption(registration_number)
        user.save(using=self._db)
        return user

class AnnualLeave(models.Model):
    annual = models.IntegerField()
    leave_count = models.IntegerField()

    class Meta:
        db_table = 'annual_leaves'

class User(AbstractBaseUser):
    WORK_TYPE = (
        ('정규', '정규 근무'),
        ('시차', '시차출퇴근')
    )

    DEFAULT_SALARY = 1822480
    
    employee_number     = models.CharField(max_length=64, unique=True)
    date_of_join        = models.DateField(max_length=64)
    annual_leave        = models.ForeignKey(AnnualLeave, on_delete=models.CASCADE)
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

    USERNAME_FIELD  = 'employee_number'
    REQUIRED_FIELDS = ['name']