#Sam Krimmel
#1/31/18
#warmup3.py - asks user for integer prints if number is divisible by 2, 3, neither, or both. 

num = int(input('Enter a number: '))

if num%2 == 0 and num%3 == 0:
    print('The number of which you have chosen is divisible by two and also happens to be divisible by three my dude.')
elif num%2 == 0:
    print('Your random heckin number is only divisible by two, what a bummer man...')
elif num%3 == 0:
    print('Ya numba is only divisible by threee.')
else:
    print("Yur number is dum, you are a failure, ya can't divide it by two or three.")
