import math
from decimal import *
a,b,c=input().split()
try:
    a=float(a)
    b=float(b)
    c=float(c)
    Delta=b**2 - 4*a*c
    can=math.sqrt(Delta)
    if a==0:
        x=-c/b
        print('Phuong trinh co mot nghiem duy nhat: x ={}'.format(x))
    elif Delta <0 or a==0 and b==0:
        print('Phuong trinh vo nghiem')
    elif Delta==0:
        nghiemkep=-b/(2*a)
        print('Phuong trinh co nghiem kep: x1 = x2 = ',nghiemkep)
    elif Delta >0:
        x1=(-b +can)/2*a
        x2=(-b -can)/2*a
        print('Phuong trinh co hai nghiem phan biet: x1={},x2={}'.format(x1,x2))
    elif a==0 and b==0 and c==0:
        print('Phuong trinh co vo so nghiem!')
except:
    print('Dinh dang dau vao khong hop le!')