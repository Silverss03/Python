class Matrix:
    def __init__(self, matrix, n, m) :
        self.matrix = matrix
        self.r = n 
        self.c = m 
    def multiply(self):
        res_m = [[0]*self.r for _ in range(self.r)] 
        for i in range(self.r):
            for j in range(self.r):
                for k in range(self.c):
                    res_m[i][j] += self.matrix[i][k] * self.matrix[j][k]
        for i in range(len(res_m)):
            for j in range(len(res_m[0])):
                print(res_m[i][j], end= " ")
            print()

for t in range(int(input())):
    n, m = [int(i) for i in input().split()]
    matrix = [[0]*m for _ in range(n)] 
    for i in range(n):
        ls = [int(k) for k in input().split()]
        for j in range(m):
            matrix[i][j] = ls[j]
    a = Matrix(matrix, n, m)
    a.multiply()