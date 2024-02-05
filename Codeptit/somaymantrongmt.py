n, m = [int(i) for i in input().split()]
matrix = []
pos = []
n1, n2  = -1, 10001 
for i in range(n):
    arr = [int(i) for i in input().split()]
    for j in range(m):
        if(arr[j] < n2):
            n2 = arr[j]
        if(arr[j] > n1):
            n1 = arr[j]
    matrix.append(arr)
lucky = n1 - n2 
for i in range(n):
    for j in range(m):
        if(matrix[i][j] == lucky):
            pos.append((i,j))
if(len(pos) > 0) :
    print(lucky)
    for i in pos :
        print("Vi tri [{}][{}]".format(i[0], i[1]))
else:
    print("NOT FOUND")

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 67 28 23
# 29 77 11 67
# 16 51 24 21
# 13 25 77 77