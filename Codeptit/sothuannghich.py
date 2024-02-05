def convert(n, k):
    res = ""
    while(n != 0):
        res += str(n % k)
        n = int(n/k)
    return res[::-1] == res
a, b, m = [int(i) for i in input().split()]
res = 0
arr = []
for i in range(a,b + 1):
    check = True
    for j in range(2, m + 1):
        if not convert(j,i):
            check = False
            break
    if(check):
        res += 1
print(res)
            
