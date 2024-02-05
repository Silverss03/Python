n = int(input())
arr = [[[0] for i in range(n)] for j in range(n)]
up = down = 0 
for i in range(n):
    inp = [int(i) for i in input().split()]
    for j in range(n):
        arr[i][j] = inp[j]
k = int(input())
for i in range(n):
    for j in range(n):
        if(i < j):
            down += arr[i][j]
        elif(i > j):
            up += arr[i][j]
diff = abs(up - down)
if(diff <= k):
    print("YES")
else:
    print("NO")
print(diff)