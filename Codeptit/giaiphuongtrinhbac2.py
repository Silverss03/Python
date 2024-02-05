a, b, c = [int(i) for i in input("Nhap 3 so a b c:\n").split()]
delta = b*b -4*a*c
if(delta < 0):
    print("Vo nghiem")
else:
    if(a!= 0):
        x1 = int((-b + delta**0.5)/(2*a))
        x2 = int((-b - delta**0.5)/(2*a))    
        if(delta == 0):
            print(x1)
        else:
            print(str(x1) + " " + str(x2))
    else:
        if(b == 0 and c == 0):
            print("Vo so nghiem")
        elif(b == 0 and c != 0):
            print("Vo nghiem")
        else:
            print(-c/b)
            