for t in range(int(input())):
    n, p = [int(i) for i in input().split()]
    cnt = 0 
    for i in range(p, n + 1, p):
        tmp = i
        while(tmp % p == 0):
            cnt += 1
            tmp = (int)(tmp/p)
    print(cnt)