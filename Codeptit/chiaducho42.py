time = [1] * (42)
cnt = 0 
l = 10 
while(l != 0):
    arr = [int(i) for i in input().split()]
    l -= len(arr)
    for i in range(len(arr)):
        tmp = arr[i] % 42 
        if(time[tmp] == 1):
            cnt += 1
            time[tmp] += 1
print(cnt )