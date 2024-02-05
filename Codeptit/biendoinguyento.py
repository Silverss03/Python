import math
def isPrime(n):
    if(n < 2):
        return False
    for i in range(2, int(n**(0.5)) + 1):
        if(n % i == 0):
            return False
    return True

def inc(n):
    cnt = 0 
    while not isPrime(n + cnt): cnt += 1 
    return cnt

def dec(n):
    cnt = 0 
    while not isPrime(n - cnt) and n - cnt >= 2: cnt += 1
    return cnt if cnt < n - 1 else math.inf
n = int(input())
arr = [int(i) for i in input().split()]
res = 0 
for i in arr :
    if not isPrime(i):
        if(dec(i) > inc(i)):
            res = max(res, inc(i))
        else:
            res = max(res, dec(i))
print(res)