from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()
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
