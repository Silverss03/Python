n = int(input())
arr = [[[0] for i in range(n)] for j in range(n)]
up = down = 0 
for i in range(n):
    inp = [int(i) for i in input().split()]
    for j in range(n):
        arr[i][j] = inp[j]
k = int(input())
for i in range(n):
    for j in range(n - i - 1):
        up += arr[i][j]
    for j in range(n - i, n):
        down += arr[i][j]
diff = abs(up - down)
if(diff <= k):
    print("YES")
else:
    print("NO")
print(diff)

# 5
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9
# 5