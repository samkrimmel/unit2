#Sam Krimmel
#2/12/18
#quiz2.py - Conditional statements

word1 = input('Enter a word: ')
word2 = input('Enter another word: ')

if 'p' in word1 and 'p' in word2:
    print('Both words have a p')
elif 'p' in word1:
    print('Only the first word has a p')
elif 'p' in word2:
    print('Only the second word has a p')

num1 = int(input('Enter two numbers that add up to 12, enter first number: '))
num2 = int(input('Enter second number: '))

if num1 + num2 == 12:
    print('CORRECT!')
else:
    print('INCORRECT!')
