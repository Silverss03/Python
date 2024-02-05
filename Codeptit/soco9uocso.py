import math
def divisor(n):
    res = 0
    lim = int(n ** 0.5)
    prime = [i for i in range(lim + 1)]
    for i in range(2, lim + 1):
        if(prime[i] == i):
            for j in range(i * i, lim + 1 , i):
                prime[j] = i
    for i in range(2, lim + 1):
        p = prime[i]
        q = prime[i//p]
        if(p != q and q != 1 and p*q == i):
            res += 1
        elif(prime[i] == i and math.pow(i, 8) <= n):
            res += 1
    return res
print(divisor(int(input())))