import jwt

from rest_framework.response import Response
from django.utils import timezone

from users.models import User
from my_settings import SECRET
from users.utils.roles import get_roles

def validate_login(func):
    def wrapper(self, request, *args, **kwargs):
        access_token = request.headers.get("Authorization", None)
        if not access_token:
                return Response({'message': '로그인 해주세요'}, status=401)
        access_token_payload = jwt.decode(
            access_token,
            SECRET,
            algorithms="HS256"
            )
    
        try:
            user = User.objects.get(employee_number=access_token_payload.get('employee_number', None))
        except User.DoesNotExist:
            return Response({'message': '다시 로그인 해주세요'}, status=401)

        now = timezone.now().timestamp()
        if now > access_token_payload['iat'] + timezone.timedelta(minutes=10).seconds:
            refresh_token_payload = jwt.decode(
                    user.refresh_token,
                    SECRET,
                    algorithms="HS256"
                    )
            if now > refresh_token_payload['iat'] + timezone.timedelta(weeks=2).seconds:
                return Response({'message': 'refresh_token_expired'}, status=401)
            else:
                access_token = jwt.encode(
                    {
                        'user_id': user.id,
                        'iat'    : now
                    },
                    SECRET,
                    algorithm = 'HS256'
                    )
                return Response({'message': 'access_token_refreshed', 'access_token': access_token}, status=401)
        else:
            request.user = user
        
        return func(self, request, *args, **kwargs)
    return wrapper

def is_admin(func):
    def wrapper(self, request, *args, **kwargs):
        roles = get_roles(request.user.employee_number)
        print(roles)
        if "관리자" not in roles.values():
            return Response({'message':'관리자가 아닙니다'}, status=403)
        return func(self, request, *args, **kwargs)
    return wrapper