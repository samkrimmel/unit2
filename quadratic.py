#Sam Krimmel
#1/28/18
#quadformula.py - implements the quadratic formula

from math import sqrt

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
dis = (b**2)-(4*a*c)

if dis < 0:
    dis = -dis
    print("The first solution is: ", complex((-b/(2*a)),((sqrt(dis))/(2*a))))
    print("The second solution is: ",complex((-b/(2*a)),-((sqrt(dis))/(2*a))))
else:
    print("The first solution is: ",(-b+(sqrt((b**2)-(4*a*c))))/(2*a))
    print("The second solution is: ",(-b-(sqrt((b**2)-(4*a*c))))/(2*a))

