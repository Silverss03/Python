try:
    with open('Bai2.9.inp','r') as file:
        a,b,c=map(float,file.readline().split())
        if a <0 or b<0 or c<0:
            with open('Bai2.9.out','w') as newfile:
                    newfile.write('Cac canh cua tam giac phai lon hon 0!')
        elif (a+b)>c and (a+c)>b and (b+c)>a:
            if a==b==c:
                with open('Bai2.9.out','w') as newfile:
                    newfile.write('{},{},{} la ba canh cua mot tam giac deu'.format(a,b,c))
            elif a==b or a==c or b==c:
                with open('Bai2.9.out','w') as newfile:
                    newfile.write('{},{},{} la ba canh cua mot tam giac can'.format(a,b,c))
            elif a**2+b**2==c**2 or a**2+c**2==c**2 or b**2+c**2==a**2:
                with open('Bai2.9.out','w') as newfile:
                    newfile.write('{},{},{} la ba canh cua mot tam giac vuong'.format(a,b,c))
            elif a**2>b**2+c**2 or b**2>a**2+c**2 or c**2>a**2+b**2:
                with open('Bai2.9.out','w') as newfile:
                    newfile.write('{},{},{} la ba canh cua mot tam giac tu'.format(a,b,c))
            else:
                with open('Bai2.9.out','w') as newfile:
                    newfile.write('{},{},{} la ba canh cua mot tam giac nhon'.format(a,b,c))
        else:
            with open('Bai2.9.out','w') as newfile:
                newfile.write('{},{},{} khong phai la ba canh cua mot tam giac'.format(a,b,c))
except FileNotFoundError:
    with open('Bai2.9.out','w') as newfile:
        newfile.write('Khong tim thay file input!')
except:
    with open('Bai2.9.out','w') as newfile:
        newfile.write('Dinh dang dau vao khong hop le!')

