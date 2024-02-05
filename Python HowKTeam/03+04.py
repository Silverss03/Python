print('Nhập tên')
c=input()
print('Xin','chào!','Tôi','tên','là',c,sep='--')
a=int(input())
print('So thap phan aM trong he bat phan la %o' % (a))
a=int(input())
dư=[]
def oct(a):
    while a>0:
        b=a%8
        dư.append(str(b))
        a=a//8
    c=len(dư)
    print('Số bát phân của số vừa nhập là:')
    while c>0:
        print(dư[c-1],end='')
        c-=1
oct(a)