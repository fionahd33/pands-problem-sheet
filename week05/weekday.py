# Wite a program that outputs whether or not today is a weekday
# Author: Fiona Healy Donnelly

## Links to code: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python


import datetime # want to import the datetime module to find if today is a weekday

IsTodayWeekday = datetime.datetime.today().weekday()
TodaysDate = datetime.datetime.today().date()

if IsTodayWeekday < 5: # Digits 0-6 represent the consecutive days of the week, starting from Monday.
    print ('Yes, unfortunately today is a weekday, {}.'.format(TodaysDate))
else:  # 5 Sat, 6 Sun
    print ('It is the weekend, yay!')