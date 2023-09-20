### Dates ###
from datetime import date, datetime, time, timedelta

# Date time
now = datetime.now()

def print_data(date_param: datetime) -> None:
    print(date_param.year)
    print(date_param.month)
    print(date_param.day)
    print(date_param.hour)
    print(date_param.minute)
    print(date_param.second)

print_data(now)

year_2023 = datetime(2023, 12, 31)
print_data(year_2023)

print('\n')

# Time
current_time = time(hour=10, minute=30, second=20)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print('\n')

# Date
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023, 1, 9)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(
    current_date.year,
    current_date.month + 1,
    current_date.day
)

print(current_date)

print('\n')

# Operaciones con fechas
diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

print('\n')

# Timedelta
start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
