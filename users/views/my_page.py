from django.db.models import F, Sum

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from schedules.models.schedules import Schedule
from users.utils.token import validate_login
from schedules.utils.date import format_str_date
from schedules.utils.time import second_to_time, get_today_commute

class MyPage(APIView):
    permission_classes = []
    @validate_login
    def get(self, request):
        employee = request.user
        data = request.data
        work_in, work_out = get_today_commute(employee)
        work_time_list = []
        total_work_time = None

        try:
            first_day = format_str_date(data['first_day'])
            last_day = format_str_date(data['last_day'])
        except KeyError:
            return Response({"message":"KEY_ERROR"}, status=400)

        schedules = Schedule.objects.filter(created_at__date__range=[first_day, last_day])\
            .select_related('user')\
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
            total_work_time = second_to_time(
                schedules.aggregate(Sum('work_time', distinct=True))['work_time__sum'].seconds)
        
        data = {
            'name':employee.name,
            'work_in':work_in,
            'work_out':work_out,
            'work_time_list':work_time_list,
            'total_work_in_week':total_work_time
            }
        return Response(data, status=status.HTTP_200_OK)