#Sam Krimmel
#2/5/18
#ageCalculator.py - Asks for user's birthday and outputs their age.

from datetime import date

year = int(input('Enter the year in which you were born: '))
month = int(input('Enter the month in which you were born: '))
day = int(input('Enter the day you were born: '))

if date.today().month == month and date.today().day == day:
    print('HAPPY BIRTHDAY!!!')
elif date.today().year - year < 0:
    print('You will be born', -1*(date.today().year - year),'years in the future.')
elif date.today().year - year == 0:
    if date.today().month - month < 0:
        print('You will be born', -1*(date.today().month - month),'months in the future.')
    elif date.today().month == month:
        if day > date.today().day:
            print('You will be born', -1*(date.today().day - day),'days in the future.')
        else:
            print('You are', date.today().day - day,'days old.')
    else:
        print('You are', date.today().month - month,'months old.')
else:
    print('You are', date.today().year - year, 'years old.')
