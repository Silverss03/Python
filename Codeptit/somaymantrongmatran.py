n, m = [int(i) for i in input().split()]
matrix = 
max = -1
min = 10001
check = False
for i in range(n):
    ls = [int(k) for k in input().split()]
    for j in range(m):
        matrix[i][j] = ls[j]
print(max - min)
luck = max - min
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end= " ")

        if(matrix[i][j] == luck):
            check = True
            #print("Vi tri [" + i+ "][" + j +"]")
    print()
if(check == False):
    print("NOT FOUND")
