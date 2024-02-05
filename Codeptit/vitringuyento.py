primes = [True] * 1000
primes[0] = primes[1] = False 
for i in range(2, 1000):
    if(primes[i]):
        for j in range(i*i, 1000, i):
            primes[j] = False

for t in range(int(input())):
    num = input()
    ok = 1 
    for i in range(len(num)):
        if(primes[i] == True and primes[int(num[i])] == False):
            ok = 0 
        if(primes[i] == False and primes[int(num[i])] == True):
            ok = 0 
    if(ok == 1):
        print("YES")
    else:
        print("NO")