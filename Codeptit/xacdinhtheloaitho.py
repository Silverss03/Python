n = int(input())
cnt = 0
ls = []
while(n > 0):
    line = input().split()
    n -= 1
    if(len(line) != 7):
        ls.append(1)
        cnt += 1
        while(True):
            if(n == 0):
                break
            line = input().split()
            n -= 1   
            if(len(line) != 6 and len(line) != 8):
                ls.append(2)
                cnt += 1
                for i in range(3):
                    line = input()
                    n -= 1           
                break
    else:
        ls.append(2)
        cnt += 1
        for i in range(3):
            line = input()
        n -= 3
print(cnt)
for i in ls:
    print(i)
            
# 8
# Minh ve minh co nho ta
# Muoi lam nam ay thiet tha man nong
# Minh ve minh co nho khong
# Nhin cay nho nui nhin song nho nguon
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay
