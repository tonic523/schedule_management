from django.db                  import models
from django.db.models.deletion  import CASCADE
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)

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
    WORK_TYPE = (
        (1, "08:00"),
        (2, "09:00"),
        (3, "10:00") 
        )
    email               = models.EmailField(max_length=255, unique=True)
    name                = models.CharField(max_length=64)
    phone_number        = models.CharField(max_length=64)
    registration_number = models.CharField(max_length=32)
    annual_leave        = models.PositiveIntegerField(default=0)
    date_of_join        = models.DateField()
    employee_number     = models.CharField(max_length=64)
    roles               = models.ManyToManyField('Role', through='UserRole', related_name='managers')
    work_type           = models.IntegerField(default=2, choices=WORK_TYPE)

    class Meta:
        db_table = 'users'

    objects = CustomUserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['name']

class Right(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'rights'

class Role(models.Model):
    name   = models.CharField(max_length=64)
    rights = models.ManyToManyField(Right, through='RoleRight', related_name='roles')

    class Meta:
        db_table = 'roles'

class RoleRight(models.Model):
    right = models.ForeignKey(Right, on_delete=CASCADE)
    role  = models.ForeignKey(Role, on_delete=CASCADE)

    class Meta:
        db_table = 'roles_rights'

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    role = models.ForeignKey(Role, on_delete=CASCADE)

    class Meta:
        db_table = 'users_roles'

