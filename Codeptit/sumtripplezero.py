for t in range(int(input())):
    n = int(input())
    arr = sorted([int(i) for i in input().split()])
    res = 0 
    for j in range(n - 2):
        l = j + 1
        r = n - 1
        while(l < r):
            tmp = arr[j] + arr[l] + arr[r]
            if(tmp == 0):
                l += 1
                res += 1
            elif(tmp > 0):
                r -= 1
            else:
                l += 1
        j += 1
    print(res)

# 2
# 5
# 0 -1 2 -3 1 
# 5
# 1 -2  1  0  5