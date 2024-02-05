res = []
n, m = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
def solve(i, arr, str, curr):
    if(curr == m):
        res.append(str)
    if(curr > m or i >= n - 1):
        return
    solve(i + 1, arr, str + "+", (curr + arr[i + 1]))
    solve(i + 1, arr, str + "-", (curr - arr[i + 1]))
    solve(i + 1, arr, str + "*", (curr * arr[i + 1]))
solve(0, arr, "", arr[1])
for i in res:
    print(arr[0], end ="")
    for j in range(len(i)):
        print(str(i[j]) + str(arr[j + 1]), end= "")
    print()


