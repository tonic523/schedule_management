from schedules.models.schedules import Schedule
from django.utils import timezone

def second_to_time(second):
    if second is None:
        return None
    else:
        hour, miniute = str(second // 3600).zfill(2), second % 3600
        miniute = str(miniute // 60).zfill(2)
        return f'{hour}:{miniute}'

def work_status(work_time, due_time ,status):
    if work_time is None:
        return None
    else:
        return status if work_time.time() > due_time else None

def get_work_seconds(start_work, end_work):
    if start_work < end_work.time():
        return (end_work.time() - start_work).seconds
    else:
        return None

def format_time(time):
    FORMAT = '%H:%M'
    return time.strftime(FORMAT) if time else None

def get_today_commute(employee):
    try:
        today_schedule = Schedule.objects.get(user=employee, created_at__date = timezone.now().strftime('%Y-%m-%d'))
        created_at = today_schedule.created_at
        updated_at = today_schedule.updated_at
    except Schedule.DoesNotExist:
        created_at = None
        updated_at = None
    return created_at, updated_at