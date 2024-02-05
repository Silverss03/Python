num = int(input()) 
arr = list(map(int, input().split()))
idx = 0
while idx < len(arr) - 1:
    if (arr[idx + 1] + arr[idx]) % 2 == 0:
        arr.pop(idx)
        arr.pop(idx)
        if idx > 0 :
            idx -= 1
    else:
        idx += 1
print(len(arr))