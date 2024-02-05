for t in range(int(input())):
    string = input()
    res = True
    for i in range (len(string)):
        if(string[i] != '4' and string[i] != '7'):
            res = False
    if(res == True):
        print("YES")
    else: print("NO")