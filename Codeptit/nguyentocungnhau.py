def GCD(a,b):
    if(b == 0): return a 
    return GCD(b, a%b)

n, k = [int(i) for i in input().split()]
start = 10**(k - 1)
end = 10**k
count = 0
for i in range(start, end):
    if(GCD(n, i) == 1):
        count += 1
        print(i, end= " ")
    if(count % 10 == 0):
        print()
        count = 0