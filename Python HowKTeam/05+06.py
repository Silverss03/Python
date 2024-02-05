try:
    a=int(input())
    dư=[]
    def oct(a):
        while a>0:
            b=a%8
            dư.append(str(b))
            a=a//8
        c=len(dư)
        print('Số bát phân của số vừa nhập là:')
        while c>0:
            print(dư[c-1],end='')
            c-=1
    oct(a)
except:
    print('Mời nhập lại')
from decimal import *
b=float(input())
a=int(input())
c='{0:.{1}f}'.format(b,a)
print(c)