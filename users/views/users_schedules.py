from django.utils import timezone

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from users.models import User
from schedules.models.schedules import Schedule

class UserSchedule(APIView):
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
