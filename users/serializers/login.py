import jwt

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler

from my_settings import SECRET
from users.utils.roles import get_permissions


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
        user = authenticate(employee_number=employee_number, password=password) # email 말고 emplyee_number와 password 로 하는 방법?
        
        if user is None:
            raise serializers.ValidationError(
                {'message':'사원번호 혹은 비밀번호를 확인해주세요'}
            )
        
        payload = {
            'employee_number':user.employee_number,
            'name':user.name,
            'permissions':get_permissions(user.employee_number),
            'iat' :timezone.now().timestamp()
        }
        
        access_token = jwt.encode(
                payload,
                SECRET,
                algorithm="HS256"
            ).decode('utf-8')

        user.refresh_token = access_token
        user.save()

        return {
        'employee_number': user.employee_number,
        'token': access_token
        }    