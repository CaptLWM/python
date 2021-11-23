# 날짜 및 시간 관련 처리 모듈
# import datetime
# datetime.date()
# datetime.time()
# datetime.datetime()

from datetime import date, time, datetime
import datetime

set_day = datetime.date(2019, 3, 1)
print(set_day)  # 2019-03-01

print('{0}/{1}/{2}'.format(set_day.year, set_day.month, set_day.day))

day1 = datetime.date(2021, 11, 23)
day2 = datetime.date(2022, 2, 25)
diff_day = day2 - day1
print(diff_day)  # 94 days, 0:00:00

print(type(day1))  # <class 'datetime.date'>
print(type(diff_day))  # <class 'datetime.timedelta'>

print(datetime.date.today())

today = datetime.date.today()
special_day = datetime.date(2021, 12, 25)
print(special_day-today)  # 32 days, 0:00:00

set_time = datetime.time(15, 30, 45)
print(set_time)
print('{0}:{1}:{2}'.format(set_time.hour, set_time.minute, set_time.second))

set_dt = datetime.datetime(2018, 10, 9, 10, 20, 0)
print(set_dt)

print('날짜 {0}/{1}/{2}'.format(set_dt.year, set_dt.month, set_dt.day))
print('시각 {0}:{1}:{2}'.format(set_dt.hour, set_dt.minute, set_dt.second))

now = datetime.datetime.now()
print(now)  # 2021-11-23 11:07:22.566009

print("Date & Time: {:%Y-%m-%d, %H:%M:%S}".format(now))
print("Date : {:%Y/%m/%d}".format(now))
print("Time : {:%H:%M:%S}".format(now))  # 따옴표 필수, 대소문자 구분
'''
Date & Time: 2021-11-23, 11:10:01
Date : 2021/11/23
Time : 11:10:01
'''

set_dt = datetime.datetime(2017, 12, 1, 12, 30, 45)
print("현재 날짜 및 시각:", now)
print("차이:", set_dt - now)


print(date(2019, 7, 1))

print(date.today())
print(time(15, 30, 45))
print(datetime(2020, 2, 14, 18, 10, 50))
print(datetime.now())
