try:
    a=int(input())
    A=65
    for i in range(a):
        Khoangtrang=" "*((a-i)*2-1)
        print(Khoangtrang,end=' ')
        for j in range(2*i+1):
            chu=chr(A)
            print(chu,end=" ")
            A+=1
        print()
except:
    print("Dinh dang dau vao khong hop le!")