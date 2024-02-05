n = int(input())
matrix = [[["."] for _ in range(n)] for _ in range(n)]
res = 0
for i in range(n):
    arr = input()
    for j in range(n):
        matrix[i][j] = arr[j]
for i in range(n):
    for j in range(n):
        if(matrix[i][j] == "C"):
            for k in range(j + 1, n):
                if(matrix[i][k] == "C"):
                    res += 1
            for k in range(i + 1, n):
                if(matrix[k][j] == "C"):
                    res += 1
print(res)

# 4
# CC..
# C..C
# .CC.
# .CC.
