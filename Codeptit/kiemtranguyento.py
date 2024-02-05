prime = [True] * 10001
for i in range(2, 10001):
    if(prime[i] == True):
        for j in range(i * i, 10001, i):
            prime[j] = False

for t in range(int(input())):
    n = input()
    if(prime[int(n[-4::])]):
        print("YES")
    else:
        print("NO")