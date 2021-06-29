import jwt

from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone

from users.models import User
from my_settings import SECRET
from users.utils.roles import get_roles

def validate_login(func):
    def wrapper(self, request, *args, **kwargs):
        access_token = request.headers.get("Authorization", None)
        if not access_token:
                return Response({'message': '로그인 해주세요'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            access_token_payload = jwt.decode(
                access_token,
                SECRET,
                algorithms="HS256"
                )
        except jwt.exceptions.DecodeError:
            return Response({'message':'인증된 유저가 아닙니다'}, status=status.HTTP_401_UNAUTHORIZED)

        now = timezone.now().timestamp()
        print(request.user)
        print(type(request.user))
        if now < access_token_payload['iat'] + timezone.timedelta(days=30).total_seconds():
            try:
                user = User.objects.get(employee_number=access_token_payload.get('employee_number', None))
                request.user = user
            except User.DoesNotExist:
                return Response({'message': '다시 로그인 해주세요'}, status=401)
        else:
            return Response({'message': '다시 로그인해주세요'}, status=401)
        print(request.user)
        return func(self, request, *args, **kwargs)
    return wrapper

def is_admin(func):
    def wrapper(self, request, *args, **kwargs):
        roles = get_roles(request.user.employee_number)
        if "관리자" not in roles.values():
            return Response({'message':'관리자가 아닙니다'}, status=403)
        return func(self, request, *args, **kwargs)
    return wrapper