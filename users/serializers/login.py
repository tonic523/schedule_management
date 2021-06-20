from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler

User = get_user_model()

def jwt_payload_handler(user):
    return {
        'employee_number':user.employee_number,
        'name':user.name
    }

class UserLoginSerializer(serializers.Serializer):
    employee_number = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        employee_number = data.get("employee_number", None)
        password = data.get("password", None)

        try:
            user = User.objects.get(employee_number=employee_number)
            email = user.email
            user_email = authenticate(email=email, password=password) # email 말고 emplyee_number와 password 로 하는 방법?
            
            if user_email is None:
                raise serializers.ValidationError(
                    {'message':'비밀번호를 확인해주세요'}
                )
            
            payload = jwt_payload_handler(user_email)
            jwt_token = jwt_encode_handler(payload)

            return {
            'employee_number': user.employee_number,
            'token': jwt_token
            }

        except User.DoesNotExist:
            raise serializers.ValidationError(
                {'message':'사원번호를 확인해주세요'}
            )