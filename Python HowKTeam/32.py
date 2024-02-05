try:
    a=int(input())
    giaithua=1
    if a<0:
        print('Vui long nhap so tu nhien!')
    elif a==0:
        print(1)
    else:
        for i in range(a,0,-1):
            giaithua*=i
        print(giaithua)
except:
    print('Dinh dang dau vao khong hop le!')