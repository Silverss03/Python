from decimal import *
try:
    print('Mời nhập số thập phân')
    a=float(input())
    print('Bạn muốn làm tròn số này đến ?')
    b=int(input())
    c='{0:.{1}f}'.format(a,b)
    print('Số '+str(a)+' làm tròn đến '+str(b)+' số thập phân là '+str(c))
except:
    print('Mời nhập lại')
print('Mời nhập dãy số')
try:
    a=list(input().split())
    print('Tổng của dãy số là',sum(list(map(int,a))))
except:
    print('Dãy số đầu vào không hợp lệ')


