from os import write

try:
    with open('Bai2.10.inp','r') as file:
        a=file.readline().rstrip()
        b=int(file.readline())
        result='Vao 20 nam nua, tuoi cua  {}  se la  {}'.format(a,b)
    with open('Bai1.10.out','w') as anotherfile:
        anotherfile.write('{}'.format(result))
except:
    print('Khong tim thay file input!')
