def con(window):
    check = False
    for i in range(len(window)):
        if(window.count(window[i]) == 1):
            check = True
    return check 
for t in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    check = True
    for i in range(2, n):
        window = []
        minor_check = True 
        for j in range(0,i):
            window.append(arr[j])
        minor_check = con(window)
        print(window)
        for j in range(i, n):
            window.remove(arr[j - i])
            window.append(arr[j])
            print(window)
            minor_check = con(window)
            print(minor_check)
        if(minor_check == False):
            check = False 
            break
    if(check):
        print("YES")
    else:
        print("NO")