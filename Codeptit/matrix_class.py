class Matrix:
    def __init__(self, matrix, n, m) :
        self.matrix = matrix
        self.r = n 
        self.c = m 
    def tranpose(self):
        trans_m = [[0]*self.r for _ in range(self.c)] 
        for i in range(len(trans_m)):
            for j in range(len(trans_m[0])):
                trans_m[i][j] = self.matrix[j][i]
        return trans_m
    def multiply(self, object):
        res_m = [[0]*self.r for _ in range(self.r)] 
        for i in range(len(self.matrix)):
            for j in range(len(object.matrix[0])):
                for k in range(len(object.matrix)):
                    res_m[i][j] += self.matrix[i][k] * object.matrix[k][j]
        for i in range(len(res_m)):
            for j in range(len(res_m[0])):
                print(res_m[i][j], end= " ")
            print()
    def out(self):
        for i in range(self.r):
            for j in range(self.c):
                print(self.matrix[i][j], end= " ")
            print()

for t in range(int(input())):
    n, m = [int(i) for i in input().split()]
    matrix = [[0]*m for _ in range(n)] 
    for i in range(n):
        ls = [int(k) for k in input().split()]
        for j in range(m):
            matrix[i][j] = ls[j]
    a = Matrix(matrix, n, m)
    b = Matrix(a.tranpose(), m,n )
    a.multiply(b)