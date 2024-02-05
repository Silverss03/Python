for t in range(int(input())):
    inp = input()
    ok = 1
    for i in range(len(inp)):
        if(i < len(inp) - 2 and inp[i] != inp[i + 2]):
            ok = 0 
    if(ok == 1):
        print("YES")
    else:
        print("NO")