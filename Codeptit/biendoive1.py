while(True):
    n = int(input())
    if(n == 0):
        break 
    else:
        cnt = {} 
        cnt[n] = 1 
        res = 1
        while(n != 1):
            if(n % 2 == 0):
                n /= 2 
            else:
                n = n * 3 + 1
            if n not in cnt :
                res += 1
            else:
                cnt[n] = 1 
        print(res)
