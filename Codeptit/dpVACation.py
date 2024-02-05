n = int(input())
arr  = []
dp = [[0] * 4 for _ in range(n)]

for i in range(n):
    arr.append([int(x) for x in input().split()])
dp[0]=arr[0]
for i in range(1,n):
  for j in range(4):
    for k in range(4):
      if k!=j:
        dp[i][j] = max(dp[i-1][k] + arr[i][j], dp[i][j])

print(max(dp[n-1]))