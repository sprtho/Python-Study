import datetime, time

now = datetime.datetime.now()

print(now.year, now.month, now.day)

print('{}-{}-{}'.format(now.year,now.month,now.day))

print(datetime.date.today())