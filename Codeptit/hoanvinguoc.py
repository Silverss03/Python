res = []
def act(i, n):
    for j in range(1, n + 1):
        if check[j] == 0:
            check[j] = 1
            arr[i] = j
            if i == n:
                string = ""
                for k in range(1, n + 1):
                    string += str(arr[k])
                res.append(string)
            else:
                act(i + 1, n)
            check[j] = 0
for t in range(int(input())):
    res.clear()
    n = int(input())
    arr = [0] * (n + 1)
    check = [0] * (n + 1)
    act(1, n)
    res.reverse()
    print(len(res))
    print(*res)