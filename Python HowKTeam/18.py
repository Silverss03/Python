from decimal import *
a,b,c=input().split()
a=float(a)
c=float(c)
if b==':' and c==0:
    print('So chia phai khac 0!')
elif b=='+':
    Plus=a+c
    print(str(a)+str(b)+str(c)+'='+str(Plus))
elif b=='-':
    Minus=a-c
    print(str(a)+str(b)+str(c)+'='+str(Minus))
elif b=='x':
    Multipile=a*c
    print(str(a)+str(b)+str(c)+'='+str(Multipile))
elif b==':':
    Divide=a/c
    print(str(a)+str(b)+str(c)+'='+str(Divide))
