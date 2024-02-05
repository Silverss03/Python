n = int(input())
matrix = []
for i in range(n):
    inp = [int(i) for i in input().split()]
    matrix.append(inp)
k = int(input())
up = 0
down = 0
for i in range(n):
    for j in range(n):
        if(i < j):
            up += matrix[i][j]
        elif(i > j):
            down += matrix[i][j]
diff  = abs(up - down)
if(diff > k):
    print("NO")
else:
    print("YES")
print(diff)

# 5
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9
# 5