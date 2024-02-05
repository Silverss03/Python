n, m = [int(i) for i in input().split()]
arr = set([int(i) for i in input().split()])
arr2 = set([int(i) for i in input().split()])
res = []
res2 = []
res3 = []
for i in arr :
    if i in arr2:
        res.append(i)
    if i not in arr2 :
        res2.append(i)
for i in arr2 :
    if i not in arr:
        res3.append(i)
res.sort()
res2.sort()
res3.sort()
print(*res)
print(*res2)
print(*res3)

# 5 6
# 1 2 3 4 5
# 3 4 5 6 7 8