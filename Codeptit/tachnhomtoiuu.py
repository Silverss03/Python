n, k = [int(i) for i in input().split()]
res = 1
arr = sorted([int(i) for i in input().split()])
for i in range(1, len(arr)):
    if(arr[i] - arr[i - 1] > k):
        res += 1
print(res)

# 7 1
# 2 6 1 7 3 4 9

