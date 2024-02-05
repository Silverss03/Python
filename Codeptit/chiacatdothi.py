out = 0
def DFS(i, List, check):
    global out
    check[i] = 1
    for x in List[i]:
        if check[x] == 0 and x != out:
            DFS(x, List, check)

for t in range(int(input())):
    res = 0
    vertex = []
    mp = {}
    v, e = [int(x) for x in input().split()]
    check = [0] * 1002
    List = [[] for _ in range(v + 1)]
    for i in range(e):
        x, y = [int(x) for x in input().split()]
        List[x].append(y)
        List[y].append(x)
    for i in range(1, v + 1):
        if(check[i] == 0):
            DFS(i, List, check)
            res += 1
    check = [0] * 1002
    for i in range(1, v + 1):
        out = i
        cnt = 0 
        for j in range(1, v + 1):
            if(check[j] == 0 and j != out):
                DFS(j, List, check)
                cnt += 1
        check = [0] * 1002
        if(cnt > res):
            res = cnt
            mp[i] = cnt
            vertex.append(i)
    if(len(vertex) > 0):
        vertex.sort()
        for i in vertex:
            if(mp[i] == res):
                print(i)
                break
    else:
        print("0")

# 2
# 5 5
# 1 2
# 1 3
# 2 3
# 3 4
# 3 5
# 5 7
# 1 2
# 1 3
# 2 3
# 2 5
# 3 4
# 3 5
# 4 5