n = int(input())
arr = sorted([int(i) for i in input().split()])
pos = n
check = 0 
print(max(arr[0] * arr[1] * arr[-1], arr[-1] * arr[-2] * arr[-3]))