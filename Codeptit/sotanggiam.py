for t in range(int(input())):
    n = input()
    d = [0] * 10
    l = 0
    ok = 1
    count = 0 
    if(len(n) < 3):
        print("NO")
    else:
        while(l < len(n)):
            if(d[int(n[l])] == 0):
                d[int(n[l])] = 1
                count += 1 
            if(n[l] < n[l + 1]):
                l+= 1
            else:
                break
        while(l < len(n) - 1):
            if(d[int(n[l])] == 0):
                d[int(n[l])] = 1
                count += 1 
            if(n[l] > n[l + 1]):
                l += 1
            else:
                ok = 0 
                break
        if(d[int(n[-1])] == 0):
            count += 1
        if(ok == 1 and count >= 3):
            print("YES")
        else:
            print("NO")