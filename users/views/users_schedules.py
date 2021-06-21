from django.utils import timezone

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.views import APIView

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

class UserSchedule(APIView):

    permission_classes = []

    def post(self, request, employee_number):
        try:
            employee = User.objects.get(employee_number = employee_number)
            today = timezone.now()
            today_date = today.strftime('%Y-%m-%d')
            try:
                today_work = Schedule.objects.get(user = employee, created_at__date = today_date)
            except Schedule.DoesNotExist:
                today_work = None

            if today_work is None:
                Schedule.objects.create(
                    user = employee,
                    created_at = today,
                    get_in_time = employee.get_in_time,
                    get_off_time = employee.get_off_time
                    )
            else:
                today_work.updated_at = today
                today_work.save()
            
            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
