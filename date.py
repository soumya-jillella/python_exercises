from datetime import date,timedelta,datetime
today = date.today()
yesterday = today - timedelta(days=1)
curr_hour = datetime.now().time().hour
weekday = today.isoweekday()
print(today)
print(yesterday)
print(curr_hour)
print(weekday)