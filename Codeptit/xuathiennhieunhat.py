for t in range(int(input())):
    n = int(input())
    arr = sorted([int(i) for i in input().split()])
    max = 1
    res = arr[0]
    cnt = {}
    for i in arr:
        if i in cnt :
            cnt[i] += 1
            if(cnt[i] > max):
                max = cnt[i]
                res = i 
        else:
            cnt[i] = 1
    if(max * 2 <= n):
        print("NO")
    else:
        print(res)
