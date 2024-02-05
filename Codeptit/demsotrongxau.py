for t in range(int(input())):
    n = input()
    num = input()
    cnt = 0 
    l = 0 
    while(l <= len(n) - len(num)):
        ok = 1 
        tmp = l 
        for i in range(len(num)):
            if(n[tmp] != num[i]):
                ok = 0 
                break 
            else:
                tmp+=1
        if(ok == 1):
            cnt += 1
            l = tmp 
        else:
            l += 1
    print(cnt)