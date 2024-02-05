import math
try:
    with open('Bai2.10.inp') as file:
        choice=int(file.readline())
        if choice==1:
            with open('Bai2.10.inp') as file:
                read=file.read().splitlines()
                result=' '.join(read).split()
                a=float(result[1])
                b=float(result[2])
            if a==0 and b!=0:
                with open('Bai2.10.out','w') as final:
                    final.write('Phuong trinh vo nghiem')
            elif a==0 and b==0:
                with open('Bai2.10.out','w') as final:
                    final.write('Phuong trinh co vo so nghiem')
            else:
                x=-b/a
                with open('Bai2.10.out','w') as final:
                    final.write('Phuong trinh co mot nghiem duy nhat: x ={}'.format(x))
        elif choice==2:
            with open('Bai2.10.inp') as file:
                read=file.read().splitlines()
                a,b,c=map(float,read[1].split())
                Delta=b**2 - 4*a*c
                if a==0:
                    x=-c/b
                    with open('Bai2.10.out','w') as final:
                        final.write('Phuong trinh co mot nghiem duy nhat: x ={}'.format(x))
                elif Delta <0 or a==0 and b==0:
                    with open('Bai2.10.out','w') as final:
                        final.write('Phuong trinh vo nghiem')
                elif Delta==0:
                    nghiemkep=-b/(2*a)
                    can=math.sqrt(Delta)
                    with open('Bai2.10.out','w') as final:
                        final.write('Phuong trinh co nghiem kep: x1 = x2 = {} '.format(nghiemkep))
                elif Delta >0:
                    can=math.sqrt(Delta)
                    x1=(-b +can)/2*a
                    x2=(-b -can)/2*a
                    with open('Bai2.10.out','w') as final:
                        final.write('Phuong trinh co hai nghiem phan biet:\n x1={} \n x2={}'.format(x1,x2))
                elif a==0 and b==0 and c==0:
                    with open('Bai2.10.out','w') as final:
                        final.write('Phuong trinh co vo so nghiem!')
        else:
            with open('Bai2.10.out','w') as final:
                final.write('Chon 1 trong 2 chuc nang sau \n 1. Giai phuong trinh bac nhat \n 2. Giai phuong trinh bac hai')
except FileNotFoundError:
    with open('Bai2.10.out','w') as final:
        final.write('Khong tim thay file input!')
except:
    with open('Bai2.10.out','w') as final:
        final.write('Dinh dang dau vao khong hop le!')