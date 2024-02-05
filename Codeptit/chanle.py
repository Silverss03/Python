for t in range(int(input())):
    n = int(input())
    curr = n % 10 
    sum = curr 
    n = int(n/10)
    res = True
    while(n > 0):
        tmp = n % 10 
        n = int(n/10)
        if(abs(tmp - curr) != 2):
            res = False
            break 
        sum += tmp 
        curr = tmp 
    if(sum % 10 != 0):
        res = False
    if(res):
        print("YES")
    else:
        print("NO")