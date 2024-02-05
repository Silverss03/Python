def GCD(a,b):
    if(b == 0): return a 
    return GCD(b, a%b)

for t in range(int(input())):
    n = int(input())
    tmp = n 
    reverse = 0 
    while(n > 0):
        reverse = reverse * 10 + (n%10)
        n = int(n/10)
    if(GCD(tmp, reverse) == 1):
        print("YES")
    else : 
        print("NO")