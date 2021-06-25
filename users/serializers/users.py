from rest_framework import serializers

from b2tech_intern_20.settings import AUTH_USER_MODEL
from users.models import User
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'employee_number',
            'date_of_join',
            'phone_number',
            'email',
            'name',
            'work_type',
            'salary',
            'get_in_time',
            'get_off_time',
            'remaining_annual_leave',
            'annual_leave'
            )