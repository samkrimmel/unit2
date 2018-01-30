#Sam Krimmel
#1/30/18
#compoundDemo.py - how to use and/or

num = int(input('Enter a number: '))

if num > 0 and num%7 == 0:
    print(num, 'is positive and divisible by seven!')
elif num > 0 and num%7 != 0:
    print(num, 'is positive but not divisible by seven.
else:
    print('ERROR. FBI HAS HACKED YOUR COMPUTER.')

