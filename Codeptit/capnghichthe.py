n = int(input())
arr = [int(i) for i in input().split()]
cnt = 0 
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if(arr[j] < arr[i]):
            cnt+=1
print(cnt) 