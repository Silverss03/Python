for t in range(int(input())):
    inp = input()
    sum = 0 
    ls = []
    for i in range(len(inp)):
        if(inp[i].isalpha()):
            ls.append(inp[i])
        else:
            sum += int(inp[i])
    ls.sort()
    for i in ls:
        print(i,end="")
    print(sum)

# 2
# AC2BEW3
# ACCBA10D2EW30