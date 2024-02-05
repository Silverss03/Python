#ax^2+bx+c = 0
import math
a = int(input())
b = int(input())
c = int(input())
delta = b**2 - 4*a*c
x1, x2 = (int)(-b + (int)(math.sqrt(delta)))/(2*a), (int)(-b - (int)(math.sqrt(delta)))/(2*a)
if(delta == 0):
    print(x1)
elif(delta > 0):
    print(x1, x2) 
else:
    print("Vo nghiem")