for t in range(int(input())):
    n = input() 
    arr = list([int(i) for i in input().split()])
    ge = max(arr)
    le = min(arr)
    arr.sort()
    cnt = 0 
    while(le <= ge):
        if le not in arr:
            cnt += 1
        le += 1
    print(cnt)

# 2
# 5
# 4 5 3 8 6
# 3
# 2 1 3