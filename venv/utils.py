import datetime

def get_first_and_last_day_of_month(year, month):
    first_day_of_month = datetime.date(year, month, 1)
    last_day_of_month = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    start_of_week = first_day_of_month.weekday()
    return first_day_of_month, last_day_of_month, start_of_week
