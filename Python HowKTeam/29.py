try:
    a=int(input())
    if a>9 or a<1:
        print('Vui long nhap gia tri tu 1 den 9!')
    for hang in range(1,a +1):
        for cot in range(1, hang +1):
            print(cot,end=" ")
        print()
except:
    print('Dinh dang dau vao khong hop le!')
