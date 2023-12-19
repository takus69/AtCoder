import datetime


Y, M, D = map(int, input().split('/'))
day = datetime.datetime(Y, M, D)
while True:
    str_day = day.strftime('%Y/%m/%d')
    Y, M, D = map(int, str_day.split('/'))
    if Y % (M*D) == 0:
        print(str_day)
        break
    day += datetime.timedelta(days=1)
