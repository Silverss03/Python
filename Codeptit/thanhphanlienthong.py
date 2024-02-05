def DFS(i):
    check[i] = 1
    for x in graph[i]:
        if(check[x] == 0):
            DFS(x) 
n, m, v = [int(i) for i in input().split()]
graph = [[] for _ in range(n + 1)]
check = [0] * 1001
for i in range(m):
    x, y = [int(i) for i in input().split()]
    graph[x].append(y)
    graph[y].append(x)
DFS(v)
for i in range(1, n + 1):
    if(check[i] == 0):
        print(i)

# 6 4 2
# 1 3
# 2 3
# 1 2
# 4 5