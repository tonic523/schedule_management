def second_to_time(second):
    if second is None:
        return None
    else:
        hour, miniute = second // 3600, second % 3600
        miniute = miniute // 60
        return f'{hour}:{miniute}'

def work_status(time, status):
    if time is None:
        return None
    elif status == '지각':
        return status if time > 0 else None
    elif status == '연장':
        return status if time > 0 else None
        

def get_overtime(time):
    if time is None:
        return None
    else:
        return time if time > 0 else None