for t in range(int(input())):
    sum = 0 
    n = input()
    ok = 1
    tmp = n[0]
    for i in range(len(n)):
        sum += int(n[i])
        if(i != 0 and i % 2 == 0):
            if(tmp != n[i]):
                ok = 0 
            else:
                tmp = n[i] 
    if(n[0] != n[1] and len(n) % 2 != 0 and ok == 1):
        print("YES")
    else:
        print("NO")
    