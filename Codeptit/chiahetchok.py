a, k, n = [int(i) for i in input().split()]
res = -1
inc = k 
while(k <= n):
    if(k - a > 0) : 
        print(k - a, end= " ")
        res = 0
    k += inc
if(res == -1 ): print(res)