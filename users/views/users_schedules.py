from django.utils import timezone, dateformat

# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from users.models import User
from schedules.models.schedules import Schedule

# class UserSchedule(APIView):
#     permission_classes = []

#     def get(self, request):
#         employee_number = request.GET.get('employee_number', None)
#         employee = User.objects.filter(employee_number=employee_number)
#         if employee.exists():
#             employee


#     def post(self, request, id):
#         employee = User.objects.get(id=id)
#             if employee.exists():
#                 Schedule.objects.create(
#                     user = employee
#                 )
#                 return Response({'message': 'test'})

@api_view(['POST'])
@permission_classes([])
def record_commute(request, employee_number):
    FORMAT_FOR_RECORD = 'Y-m-d H:i:s'
    try:
        employee = User.objects.get(employee_number = employee_number)
        today = dateformat.format(timezone.now(), FORMAT_FOR_RECORD)
        today_date = today.split(' ')[0]
        try:
            today_work = Schedule.objects.get(user = employee, created_at__date = today_date)
        except Schedule.DoesNotExist:
            today_work = None

        if today_work is not None:
            Schedule.objects.create(
                user = employee,
                created_at = today)
        else:
            today_work.updated_at = today
            today_work.save()
        
        return Response(status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
