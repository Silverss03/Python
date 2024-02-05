def isReversible(n):
    if(str(n) == str(n)[::-1] and len(str(n)) > 1):
        return True
    return False
n, m = [int(i) for i in input().split()]
matrix = []
pos = []
max = -1
for i in range(n):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)
for i in range(n):
    for j in range(m):
        if(isReversible(matrix[i][j]) and matrix[i][j] > max):
            pos.clear()
            max = matrix[i][j]
            pos.append((i,j))
        elif(isReversible(matrix[i][j]) and matrix[i][j] == max):
            pos.append((i,j))
if(len(pos) > 0) :
    print(max)
    for i in pos :
        print("Vi tri [{}][{}]".format(i[0], i[1]))
else:
    print("NOT FOUND")

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 29 28 23
# 29 77 11 19
# 16 26 24 21
# 13 25 77 77