primes = [True] * 1001
primes[0] = primes[1] = False
for i in range(2, 1001):
    if(primes[i]):
        for j in range(i*i, 1001, i):
            primes[j] = False 
n, m = [int(i) for i in input().split()]
num = [[0 for i in range (m)] for j in range(n)]
for i in range(n):
    inp = [int(i) for i in input().split()]
    for j in range(m):
        if(primes[inp[j]]):
            num[i][j] = 1
for i in range(n):
    for j in range(m):
        print(num[i][j], end= " ")
    print()