primes = [True] * 1000
primes[0] = primes[1] = False
for i in range(2, 1000):
    if primes[i] == True :
        for j in range(i * i, 1000, i):
            primes[j] = False 
for t in range(int(input())):
    sum = 0 
    n = input()
    for i in range(len(n)):
        sum += int(n[i])
    if(primes[sum]):
        print("YES")
    else:
        print("NO")
    