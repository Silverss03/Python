while(True):
    res = 0 
    arr = [int(i) for i in input().split()]
    if(arr.count(0) == 4):
        break 
    while(True):
        check = True
        if(arr.count(arr[0]) == 4):
            break
        tmp = arr.copy()
        for i in range(3):
            arr[i] = abs(tmp[i] - tmp[i + 1])
        arr[3] = abs(tmp[3] - tmp[0])
        res += 1
    print(res)