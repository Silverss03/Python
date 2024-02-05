n, x = [int(i) for i in input().split()]
prime = [True] * 10000
prime[0] = prime[1] = False
arr = list()
for i in range(2, 10000):
    if(prime[i]):
        arr.append(i)
        for j in range(i*i, 10000, i):
            prime[j] = False 
print(x, end= " ")
for i in range(n):
    x += arr[i]
    print(x , end= " ")