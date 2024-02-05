
for t in range(int(input())):
    n = int(input())
    times = 1000
    res = False
    while(times > 0):
        if(n % 7 == 0):
            res = True
            print(n)  
            break
        else:
            n = n + int(str(n)[::-1])
        times-=1
    if(res == False):
        print(-1)
            