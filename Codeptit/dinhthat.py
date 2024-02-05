def DFS(i, List, check, end):
    check[i] = 1
    for x in List[i]:
        if check[x] == 0:
            DFS(x, List, check, end)
    return True

for _ in range(int(input())):
    res = 0
    v, e, start, end = [int(x) for x in input().split()]
    check = [0] * 1002
    List = [[] for _ in range(v + 1)]
    for _ in range(e):
        x, y = [int(x) for x in input().split()]
        List[x].append(y)
    for i in range(1, v + 1):
        if(i != start and i != end ):
            check[i] = 1
            DFS(start, List, check, end)
            if(check[end] == 0):
                res += 1
            check = [0] * 1002
    print(res)



# 2
# 5 7 1 3
# 1 2
# 2 4
# 2 5
# 3 1
# 3 2
# 4 3
# 5 4
# 4 5 1 4
# 1 2
# 1 3
# 2 3
# 2 4
# 3 4