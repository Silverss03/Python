try:
    start=int(input())
    end=int(input())
    emptlist=[]
    if start >end:
        print('So thu nhat lon hon so thu hai!')
    else:
        for a in range(start,end+1):
            if a%5==0:
                emptlist.append(a)
                if len(emptlist) >10:
                    print('\nIn qua 10 so roi!')
                    break   
                print(a,end=' ')
        else:
            if len(emptlist)==0:
                print('Khong co so nao chia het cho 5')
            else:
                print('\nDa in het cac so chia het cho 5')
except:
    print('Dinh dang dau vao khong hop le!')
    

