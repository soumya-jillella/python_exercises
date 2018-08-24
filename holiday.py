from datetime import date
import holidays
#help(holidays)
print(holidays.IND())
date(2014, 1, 1) in holidays.IND()
True
date(2014, 1, 2) in holidays.IND()
False


IND_holidays = holidays.IND()
date(2014, 1, 1) in IND_holidays
True
date(2014, 1, 2) in IND_holidays
False
holidays.IND() == holidays.IND()
True
 


for date, name in sorted(holidays.IND(state='AP', years=2014).items()):
    print(date, name)