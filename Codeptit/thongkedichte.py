dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

m, n = [int(i) for i in input().split()]
matrix = [[[0] for _ in range(n)] for _ in range (m)]
res = 0 
for i in range(m):
    arr = [int(i) for i in input().split()]
    for j in range(n):
        matrix[i][j] = arr[j]

for i in range(m) :
    for j in range(n):
        if(matrix[i][j] == -1):
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if(x >= 0 and x < m and y >= 0 and y < n):
                    if(matrix[x][y] >= 0):
                        res += matrix[x][y]
                        matrix[x][y] = 0
                    elif(matrix[x][y] == -1):
                        res -= 1
print(res)

# 4 4
# 1 1 0 1
# 2 -1 4 5
# 0 0 0 0
# 1 0 2 1