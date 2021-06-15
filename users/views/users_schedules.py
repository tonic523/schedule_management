from datetime import date

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

@api_view(['GET'])
@permission_classes([])
def today_user_schedule(request):
    if request.method == 'GET':
        employee_number = request.GET.get('employee_number', None)
        try:
            employee = User.objects.get(employee_number=employee_number)
            today_year, today_month, today_day = dateformat.format(timezone.now(), 'Y-m-d H:i:s').split(' ')[0].split('-')
            employee_schedules = Schedule.objects.get(
                user = employee,
                created_at__date = date(int(today_year), int(today_month), int(today_day))
            )
            attendance = employee_schedules.created_at
            leave_work = employee_schedules.updated_at
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Schedule.DoesNotExist:
            attendance = None
            leave_work = None
        
        return Response({
            'id':employee.id,
            'name':employee.name,
            'created_at' : attendance,
            'updated_at' : leave_work
            }, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([])
def commute_record(request, id):
    try:
        employee = User.objects.get(id = id)
        today_year, today_month, today_day = dateformat.format(timezone.now(), 'Y-m-d H:i:s').split(' ')[0].split('-')
        employee_schedules, attendance = Schedule.objects.get_or_create(
            user = employee,
            created_at__date = date(int(today_year), int(today_month), int(today_day))
        )
        if not attendance:
            employee_schedules.save()
        return Response(status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
