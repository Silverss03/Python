for t in range(int(input())):
    string = input()
    ok = 1 
    for i in range(len(string)):
        if (string[i] != '0' and string[i] != '1' and string[i] != '2'):
            ok = 0 
            break
    if(ok == 1):
        print("YES")
    else:
        print("NO")