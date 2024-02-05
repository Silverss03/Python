for t in range(int(input())):
    string = input()
    l , r = 1, len(string) - 2
    res = True
    while(l <= len(string) and r >= 0):
        if(abs(ord(string[l]) - ord(string[l - 1])) != abs(ord(string[r]) - ord(string[r + 1]))): res = False
        l+=1
        r-=1
    if(res):
        print("YES")
    else:
        print("NO")