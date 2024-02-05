import math
n = int(input()) + 1
arr = [int(i) for i in input().split()] + [-1]
s, res, lim = 0, 0, max(arr)
for i in arr:
    if(i == lim):
        s += 1
    else:
        res = max(res, s)
        s = 0
print(res)