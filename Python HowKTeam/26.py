try:    
    start=int(input())
    end=int(input())
    tong=0
    if start >end:
        print('So thu nhat lon hon so thu hai!')
    else:
        for a in range(start,end+1):
            tong+=a
        print(tong)
except:
    print('Dinh dang dau vao khong hop le!')