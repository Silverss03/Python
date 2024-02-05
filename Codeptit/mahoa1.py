for t in range(int(input())):
    res = ""
    i = 0 
    inp = input()
    if(len(inp) > 1):
        while(i < len(inp) - 1):
            idx = 1
            while(i < len(inp) - 1 and inp[i] == inp[i + 1]):
                idx+=1
                i+=1
            res += str(idx)
            res += inp[i]
            i += 1
        i = len(inp) -1
        if(inp[i] != inp[i - 1]):
            res += str(1)
            res += inp[i]
        print(res)
    else:
        print(str(1) + inp)