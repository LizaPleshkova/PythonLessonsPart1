from datetime import date, datetime, timedelta
import locale


# # class date
# today = date.today()
# print(today)#2021-02-10
# print(today.day, today.month, today.year)#10 2 2021
# print(today.weekday())# 2 - индех дня недели
#
#
# #class datetime
now = datetime.now()
# now2 = datetime.today()
# print( now, now2, sep='  --  ') #2021-02-10 11:34:33.447386  -- 2021-02-10 11:34:33.447386
# print(now.day, now.month, now.year)#10 2 2021
# print(now.hour, now.minute, now.second, sep = ' -- ')#12 -- 26 -- 18
# print(now.weekday())# 2 - индекс дня недели
#
#
# days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс',]
# print(days[now.weekday()])#ср

locale.setlocale(locale.LC_ALL,'ru-Ru') # 'ru-Ru.UTF-8' с кодировкой
print(now.strftime('%a'))#Wed \ Ср
print(now.strftime("%A"))#Wednesday \ среда

print(f'Date: {now.strftime("%A, %d %b %y")}') #Date: среда, 10 фев 21
print(f'Time: {now.strftime("%H:%M:%S")}') #Time : 12:40:12

print(now.strftime('%c'))#10.02.2021 12:41:17
print(now.strftime('%x'))#10.02.2021
print(now.strftime('%X'))#12:41:17



print(now.strftime('%c'))

# добавить к дате отрезок времени - timedelta
print(now + timedelta(days=1, hours=2, minutes=10))#2021-02-11 14:54:08.122296
new_day = now + timedelta(days=1, hours=2, minutes=10)
new_day.strftime('%c')