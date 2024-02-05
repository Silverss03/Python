n, m = [int(i) for i in input().split()]
matrix = []
non = []
for i in range(n):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)
if(n > m):
    non = [0]
    while(len(non) < (n - m)):
        non.append(non[-1] + 2)
    for i in range(n):
        if(i not in non):
            for j in range(m):
                print(matrix[i][j], end = " ")
            print()
else:
    if(n < m):
        non = [1]
    while(len(non) < (m - n)):
        non.append(non[-1] + 2)
    for i in range(n):
        for j in range(m):
            if(j not in non):
                print(matrix[i][j], end = " ")
        print()
# 6 4
# 2 8 7 6
# 6 3 2 6
# 7 2 2 8
# 9 9 9 8
# 9 6 6 3
# 7 7 4 9

# 4 6
# 2 8 7 6 4 3
# 6 3 2 6 7 2
# 7 2 2 8 9 1
# 9 9 9 8 0 7