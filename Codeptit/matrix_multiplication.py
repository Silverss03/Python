for t in range(int(input())):
    n, m = [int(i) for i in input().split()]
    matrix = []
    matrix_n = [[0] *  (100) for _ in range(100)]
    for i in range(n):
        tmp = []
        while(len(tmp) != m):
            tmp += [int(i) for i in input().split()]
        matrix.append(tmp)
    for i in range(m):
        for j in range(n):
            matrix_n[i][j] = matrix[j][i] 
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(m):
                sum += matrix[i][k] * matrix_n[k][j]
            print(sum, end = " ")
        print()