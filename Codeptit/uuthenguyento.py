primes = [True] * 1000
primes[0] = primes[1] = False
for i in range(2, 1000):
    if primes[i] :
        for j in range(i * i, 1000, i):
            primes[j] = False
for t in range(int(input())):
    n = input() 
    p = n_p = 0 
    if(primes[len(n)]):
        for i in range(len(n)):
            if(primes[int(n[i])]):
                p += 1
            else:
                n_p += 1
        if(p > n_p):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    