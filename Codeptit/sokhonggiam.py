for t in range(int(input())):
    num = input()
    res = True
    for i in range(len(num) - 1):
        if(num[i] > num[i + 1]):
            res = False 
            break
    if(res):
        print("YES")
    else:
        print("NO")