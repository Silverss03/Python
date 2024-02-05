for t in range(int(input())):
    a = input()
    b = a[::-1]
    ok = 1
    for i in range(1, len(a)):
        if(abs(ord(a[i]) - ord(a[i - 1])) != abs(ord(b[i]) - ord(b[i - 1]))):
            ok = 0 
    if(ok == 1):
        print("YES")
    else:
        print("NO")