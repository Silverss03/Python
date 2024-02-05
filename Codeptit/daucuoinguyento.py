primes = [True] * 1000
primes[0] = primes[1] = False
for i in range(2, 1000):
    if primes[i] :
        for j in range(i * i, 1000, i):
            primes[j] = False
for t in range(int(input())):
    n = input()
    if(primes[int(n[-3:])] and primes[int(n[:3])]):
        print("YES")
    else:
        print("NO")