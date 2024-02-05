def find(arr):
    first = max(arr)
    sec = 0
    for i in range(1, len(arr)):
        if(arr[i] > sec and arr[i] != first):
            sec = arr[i]
    return sec
n, m = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
elect = [0] * (m + 1)
for i in arr :
    elect[i] += 1 
res = find(elect)
if(res != 0):
    for i in range(1,m + 1) : 
        if(elect[i] == res):
            print(i)
            break 
else:
    print("NONE")
# 10 4
# 2 3 1 2 3 4 1 2 3 2

# 8 4
# 1 2 3 4 4 3 2 1