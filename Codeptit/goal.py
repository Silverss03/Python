n = int(input())
idx = 0 
res = 0
if(n < 10):
    print(n)
else:
    res += 12
    a = (n - 10) //15
    b = n // 15
    print(res + (n - 10) + a * 2 - b)