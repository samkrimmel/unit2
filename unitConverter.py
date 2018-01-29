#Sam Krimmel
#1/29/18
#unitConverter.py - converts units with four possible conversions

print('1) Kilometers to Miles')
print('2) Kilograms to Pounds')
print('3) Liters to Gallons')
print('4) Celsius to Fahrenheit')

choice = int(input('Choose your conversion:'))

if choice == 1:
    num = float(input('Enter distance in Kilometers:'))
    print(num, 'Kilometers is', num/0.621371, 'miles.')
elif choice == 2:
    num = float(input('Enter weight in Kilograms:'))
    print(num, 'Kilograms is', num/2.20462, 'pounds.')
elif choice == 3:
    num = float(input('Enter a volume in liters:'))
    print(num, 'liters is', num/0.264172, 'gallons.')
elif choice == 4:
    num = float(input('Enter degrees in Celsius:'))
    print(num, 'degrees Celsius is', (num*1.8)+32, 'degrees Fahrenheit.')
else:
    print('Error!')
