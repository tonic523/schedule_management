# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
#from rest_framework_jwt.utils import jwt_decode_handler

from users.serializers.login import UserLoginSerializer

@api_view(['POST'])
@permission_classes([])
def login(request):
    serializer = UserLoginSerializer(data=request.data)

    if not serializer.is_valid(raise_exception=True):
        return Response({"message": "Request Body Error"}, status=status.HTTP_409_CONFLICT)
    
    response = {
        'token': serializer.data['token'],
        #'decode_token' : jwt_decode_handler(serializer.data['token'])
    }
    return Response(response, status=status.HTTP_200_OK)