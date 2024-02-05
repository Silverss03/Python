prime = [True] * 1000001
prime[0] = prime[1] = False
for i in range(2, 1000001):
    if(prime[i]):
        for j in range(i*i, 1000001, i):
            prime[j] = False
n = input()
arr = [int(i) for i in input().split()]
num = []
for i in arr:
    if(prime[i] and i not in num):
        print(str(i) + " " + str(arr.count(i)))
        num.append(i)
