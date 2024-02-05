def count(n, d):
    cnt = 0 
    num = 1 
    while num <= n :
        div = num * 10
        quotient = n // div
        remain = n % div
        if quotient > 0 :
            cnt += quotient * num
        if d == 0 :
            cnt -= num 
        if remain >= d * num:
            cnt += min(remain - d * num + 1, num)
        num *= 10
    return cnt
for t in range(int(input())):
    low, high = map(int,input().split())
    for d in range(10):
        print(count(high, d) - count(low - 1, d), end= " ")
    print()
# 3
# 1 9
# 10 456
# 123 2437