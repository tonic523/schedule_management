from django.db.models import Q, F

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from schedules.models.schedules import Schedule
from schedules.utils.time import work_status, get_overtime, second_to_time
from users.utils.roles import get_roles

class schedules(APIView):

    authentication_classes = []#authentication.TokenAuthentication
    permission_classes = []#permissions.IsAdminUser

    def get(self, request):
        employee_number = request.GET.get('employee_number', None)
        date = request.GET.get('date', None)

        query = Q()
        if date:
            year, month, day = date.split('-')
            month, day = month.zfill(2), day.zfill(2) 
            query.add(Q(created_at__date=f'{year}-{month}-{day}'), query.AND)
        
        if employee_number:
            query.add(Q(user__employee_number = employee_number), query.AND)

        schedules = Schedule.objects.filter(query)\
            .select_related('user')\
            .annotate(
                date = F('created_at__date'),
                attendance_time = F('created_at__time'),
                quitting_time = F('updated_at__time'),
                late_time = F('created_at__time') - F('get_in_time'),
                leaving_time = F('updated_at__time') - F('get_off_time'),
                work_time = F('updated_at__time') - F('created_at__time')
            )
        
        results = [
            {
                'employee_number':schedule.user.employee_number,
                'name':schedule.user.name,
                'get_in_time':schedule.get_in_time.strftime('%H:%M'),
                'get_off_time':schedule.get_off_time.strftime('%H:%M'),
                'work_type':schedule.work_type,
                'date':schedule.date,
                'created_at' : schedule.attendance_time.strftime('%H:%M'),
                'updated_at' : schedule.quitting_time.strftime('%H:%M'),
                'late_time' : work_status(schedule.late_time.days, "지각"),
                'leaving_status' : work_status(schedule.leaving_time.seconds, "연장"),
                'leaveing_time' : second_to_time(get_overtime(schedule.leaving_time.seconds)),
                'work_time' :second_to_time(schedule.work_time.seconds),
                'roles' : get_roles(schedule.user.employee_number)
            }for schedule in schedules]

        return Response({'schedules': results}, status=status.HTTP_200_OK)