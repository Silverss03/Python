for t in range(int(input())):
    num = int(input())
    check = [0] * 1001
    res = 1000
    max = -1
    for i in range(num):
        n = int(input())
        check[n] += 1
        if(check[n] >= max):
            max = check[n]
    for i in range(1001):
        if(check[i] == max):
            res = min(res, i)
    print(res)
