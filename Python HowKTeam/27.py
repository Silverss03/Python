try:
    a=int(input())
    if a<1 or a>9:
        print('Chi tinh duoc bang cuu chuong 1 den 9 thoi!')
    else:
        for i in range(1,10):
            tích= a*i
            print('{} x {} = {}'.format(a,i,tích))
except:
    print('Dinh dang dau vao khong hop le!')