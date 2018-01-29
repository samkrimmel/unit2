#Sam Krimmel
#1/29/18
#gradeCalculator.py - Asks user for grade and outputs letter grade

grade = int(input('What is your grade? '))

if grade >= 90:
    print('You earned an A')
elif grade >= 80:
    print('You earned a B')
elif grade >= 70:
    print('You got a C')
elif grade >= 60:
    print('You got a D')
else:
    print('Bummer, you got an F')

