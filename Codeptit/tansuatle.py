for t in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    cnt = [0] * 1000000
    res = []
    for i in arr :
        cnt[i] += 1 
        if(cnt[i] % 2 != 0):
            res.append(i)
        else:
            if(i in res):
                res.remove(i)
    print(res[0])

# 2
# 7
# 1 2 3 2 3 1 3
# 5
# 1 1 3 3 2