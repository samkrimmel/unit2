#Sam Krimmel
#1/16/18
#slope.py - calculates the slope between two points

x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
if x1 == x2:
    print('The slope is undefined, the equation of the line is X=',x1)
else:
    print('The slope is',(y2-y1)/(x2-x1))
