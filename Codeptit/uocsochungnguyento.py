check = [True for _ in range(10001)]
check[0] = check[1] = False
for i in range(2, 101):
    if check[i] == True :
        for j in range(2*i, 10000, i):
            check[j] = False

def GCD(a,b):
    if(b == 0): return a 
    return(GCD(b, a%b))

for t in range (int(input())):
    a, b = [int(i) for i in input().split()]
    n = GCD(a,b)
    sum = 0
    while(n > 0):
        sum += (n % 10)
        n = int(n/10)
    if(check[sum]):
        print("YES")
    else:
        print("NO")
