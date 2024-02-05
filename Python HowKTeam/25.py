try:
    start=float(input())
    end=float(input())
    tong=0
    a=start
    if start >end:
        print('So thu nhat lon hon so thu hai!')
    else:
        while end>=a:
            tong+=a
            a+=1
        print(tong)
except:
    print('Dinh dang dau vao khong hop le!')