from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User


class ListUsers(APIView):
    def get(self, request):
        return Response({'message': 'test'})