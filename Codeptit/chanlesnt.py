primes = [True] * 1000
primes[0] = primes[1] = False
for i in range(2, 1000):
    if primes[i] == True :
        for j in range(i * i, 1000, i):
            primes[j] = False 
for t in range(int(input())):
    sum = 0 
    n = input()
    ok = 1
    for i in range(len(n)):
        sum += int(n[i])
        if(i % 2 == 0 and int(n[i]) % 2 != 0) or (i % 2 == 1 and int(n[i]) % 2 == 0):
            ok = 0
    if(primes[sum] and ok == 1):
        print("YES")
    else:
        print("NO")
    