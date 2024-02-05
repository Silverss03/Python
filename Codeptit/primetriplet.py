max = int(1e6+1)

prime = [1] * int(max) 
prime[0] = prime[1] = 0
for i in range(2, max):
    if(prime[i] == 1):
        for j in range(2*i, max, i):
            prime[j] = 0 

for t in range(int(input())):
    res = 0
    n = int(input())
    for i in range(n - 5):
        if(prime[i] and prime[i + 6]):
            if(prime[i + 2] or prime[i + 4]):
                res+=1
    print(res)