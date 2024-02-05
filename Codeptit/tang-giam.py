for t in range(int(input())):
    n = int(input())
    a, b, f, ans = [0] * n, [0] * n, [1] * n, 0
    for i in range(n):
        a[i], b[i] = [float(i) for i in input().split()]
    for i in range(n):
        for j in range(0, i):
            if(a[i] > a[j] and b[i] < b[j]):
                f[i] = max(f[i], f[j] + 1)
    print(max(f))

# 3
# 2
# 1.0 1.0
# 1.5 0.0
# 3
# 1.0 1.0
# 1.0 1.0
# 1.0 1.0
# 6
# 1.5 9.0
# 2.0 2.0
# 2.5 6.0
# 3.0 5.0
# 4.0 2.0
# 10.0 5.5