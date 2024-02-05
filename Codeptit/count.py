n, q = [int(i) for i in input().split()]
a1 = [0] * 100001
a2 = [0] * 100001
a3 = [0] * 100001
for i in range(1, n + 1):
    s = int(input())
    if s == 1 :
        a1[i] = a1[i - 1] + 1
        a2[i] = a2[i - 1]
        a3[i] = a3[i - 1]
    elif s == 2 :
        a2[i] = a2[i - 1] + 1
        a1[i] = a1[i - 1]
        a3[i] = a3[i - 1]
    else:
        a3[i] = a3[i - 1] + 1
        a1[i] = a1[i - 1]
        a2[i] = a2[i - 1]
for i in range(1, q + 1):
    s, e = [int(i) for i in input().split()]
    print(f"{a1[e] - a1[s - 1]} {a2[e] - a2[s - 1]} {a3[e] - a3[s - 1]}")

# 6 3
# 2
# 1
# 1
# 3
# 2
# 1
# 1 6
# 3 3
# 2 4

    