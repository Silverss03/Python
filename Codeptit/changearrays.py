n, k = [int(i) for i in input().split()]
arr = sorted([int(i) for i in input().split()])
for i in range(n):
    if k > 0  and arr[i] < 0:
        arr[i] *= -1
        k -= 1
if k % 2 == 1:
    arr.sort()
    arr[0] *= -1
print(sum(arr))
