def format_str_date(date):
    if not date:
        return None
    year, month, day = date.split('-')
    month, day = month.zfill(2), day.zfill(2)
    return  f'{year}-{month}-{day}'
            