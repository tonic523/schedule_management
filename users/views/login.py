# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny
#from rest_framework_jwt.utils import jwt_decode_handler

from users.serializers.login import UserLoginSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = UserLoginSerializer(data=request.data)

    if not serializer.is_valid(raise_exception=True):
        return Response({"message": "Request Body Error"}, status=status.HTTP_409_CONFLICT)
    #'decode_token' : jwt_decode_handler(serializer.data['token'])

    response = Response({
        'message' : 'SUCCESS',
        'token': serializer.data['token'],
    },
    headers={'access_token' : serializer.data['token']}, 
    content_type= 'application/json', 
    status=status.HTTP_200_OK)
    
    return response