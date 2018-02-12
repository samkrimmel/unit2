#Sam Krimmel
#2/5/18
#ageCalculator.py - Asks for user's birthday and outputs their age.

from datetime import date

year = int(input('Enter the year in which you were born: '))
month = int(input('Enter the month in which you were born: '))
day = int(input('Enter the day you were born: '))

if date.today().month == month and date.today().day == day: #Wishes user happy brithday if today is their birthday (regardless of year)
    print('HAPPY BIRTHDAY!!!') 
elif date.today().year - year < 0: #Accounts for future births
    print('You will be born', -1*(date.today().year - year),'year(s) in the future.')
elif date.today().year - year == 0: 
    if date.today().month - month < 0: #Accounts for future births in current year
        print('You will be born', -1*(date.today().month - month),'month(s) in the future.')
    elif date.today().month == month:
        if day > date.today().day: #Accounts for future births in the current month
            print('You will be born', -1*(date.today().day - day),'day(s) in the future.')
        else: #Accounts for births in current month
            print('You are', date.today().day - day,'day(s) old.')
    else: #Accounts for births in current year
        print('You are', date.today().month - month,'month(s) old.')
else: #Accounts for births outside of current year. 
    print('You are', date.today().year - year, 'year(s) old.')
