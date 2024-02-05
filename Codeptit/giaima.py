for t in range(int(input())):
    stack = []
    inp = input()
    for i in range(len(inp)):
        if(inp[i].isalpha()):
            stack.append(inp[i])
        else :
            alpha = stack.pop()
            for j in range(int(inp[i])):
                print(alpha, end= "")
    print()