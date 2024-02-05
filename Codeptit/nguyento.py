check = [True for _ in range(10001)]
check[0] = check[1] = False


for i in range(2, 101):
    if check[i]:
        for j in range(2 *i , 10001, i):
            check[j] = False

def GCD(a, b):
    if(b == 0): return a
    return(GCD(b, a%b))

for t in range(int(input())):
    n = int(input())
    k = 0 
    for i in range(1,n):
        if(GCD(i,n)) == 1:
            k += 1 
    if(check[k]): print("YES")
    else: print("NO")