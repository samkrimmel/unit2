#Sam Krimmel
#1/29/18
#movie.py - asks user for age and prints most scandalous movie they can watch

age = int(input('Enter your age: '))

if age > 17:
    print('You can watch NC-17 movies.')
elif age >= 17:
    print('You can watch R rated movies.')
elif age >= 13:
    print('You can watch PG-13 movies.')
elif age >= 10:
    print('You can watch PG movies')
else:
    print('You can watch G rated movies')

