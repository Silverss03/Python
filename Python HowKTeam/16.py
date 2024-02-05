from decimal import *
print('Nhập 3 số bất kỳ:')
So=input().split()
a,b,c=So
try:
    a=float(a)
    b=float(b)
    c=float(c)
    if a and b and c>0:
        if a+b>c and a+c>b and b+c>a:
            print('{}, {}, {}'.format(a,b,c) + 'la ba canh cua mot tam giac')
        else:
            print('{}, {}, {}'.format(a,b,c)+' khong phai la ba canh cua mot tam giac')
    else:
        print('Cac canh cua tam giac phai lon hon 0!')
except:
    print('Dinh dang dau vao khong hop le!')