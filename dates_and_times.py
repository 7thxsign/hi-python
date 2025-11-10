import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 13, 14)
current_time = datetime.datetime.now()

target_time = datetime.datetime(2040,1,3,12,4,5)
current_time = current_time.strftime("Time:%H:%M:%S Date:%d-%m-%Y")
current_date = datetime.datetime.now()
print(current_time)

print(date)
print(today)

print(time)
print(current_time)

if target_time < current_date:
    print("Target date has passed")
else:
    print("Target date has NOT passed")