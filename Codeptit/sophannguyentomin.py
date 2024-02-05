limit = int(1e8 + 1) 
divisors = [0] * (limit + 1)

for i in range(1, limit + 1):
    for j in range(i, limit + 1, i):
        divisors[j] += 1
        
for t in range(int(input())):
    n = int(input())
    max_div = -1
    for i in range(1, n):
        if(max_div < divisors[i]):
            max_div = divisors[i]
    while(1):
        if(divisors[n] > max_div):
            print(n)
            break
        else:
            n += 1 
            