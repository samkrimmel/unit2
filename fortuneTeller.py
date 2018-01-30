#Sam Krimmel
#1/30/18
#fortuneTeller.py - tells your fortune based on a color and a number
print('Pick a color:')
print('1: red')
print('2: blue')
col = int(input('Red, or blue?'))
num = int(input('Pick a number, 1-4'))

if col == 1 and num == 1:
    print('You will win the lottery, and then lose it all gambling.')
elif col == 1 and num == 2:
    print('You will win five dollars in the lottery, invest it, and make a fortune!')
elif col == 1 and num == 3:
    print('Next time you go outside, you will be crushed by a boat.')
elif col == 1 and num == 4:
    print("Just don't go near water...")
elif col == 2 and num == 1:
    print("Looks like you'll die alone...")
elif col == 2 and num == 2:
    print('Chairs will forever be pulled out from under you.')
elif col == 2 and num == 3:
    print('You will see someone try to sit down and miss their chair. Hahah!')
elif col == 2 and num == 4:
    print('What if rain was boiling? Guess what. Now it is.')

