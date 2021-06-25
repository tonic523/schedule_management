from django.db.models import F, Sum

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from users.utils.token import validate_login
from schedules.utils.date import format_str_date
from schedules.utils.time import second_to_time, get_today_commute
from users.utils.roles import get_roles

class MyPage(APIView):
    permission_classes = []
    @validate_login
    def get(self, request):
        employee = request.user
        monday = format_str_date(request.GET.get("monday"))
        sunday = format_str_date(request.GET.get("sunday"))
        
        work_in, work_out = get_today_commute(employee)
        work_time_list = []
        total_work_time = None

        schedules = employee.schedule_set.filter(created_at__date__range=[monday, sunday])\
            .annotate(
                work_time = F('updated_at__time') - F('created_at__time')
            )

        if schedules:
            for schedule in schedules:
                if not schedule.work_time:
                    work_time = None
                else:
                    work_time = second_to_time(schedule.work_time.seconds)
                work_time_list.append(work_time)
            try:
                total_work_time = second_to_time(
                    schedules.aggregate(Sum('work_time', distinct=True))['work_time__sum'].seconds)
            except AttributeError:
                pass

        data = {
            'name':employee.name,
            'employee_number':employee.employee_number,
            'roles':get_roles(employee.employee_number),
            'work_in':work_in,
            'work_out':work_out,
            'work_time_list':work_time_list,
            'total_work_in_week':total_work_time
            }
        return Response(data, status=status.HTTP_200_OK)