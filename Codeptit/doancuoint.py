primes = [True] * 10001
primes[0] = primes[1] = False
for i in range(2, 10001):
    if primes[i]:
        for j in range(i*i, 10001,i):
            primes[j] = False
            
for t in range(int(input())):
    n = input()
    end = int(n[-4:])
    if(primes[end]):
        print("YES")
    else:
        print("NO")