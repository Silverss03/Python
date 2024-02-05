for t in range(int(input())):
    n = int(input())
    arr1 = sorted([int(i) for i in input().split()])
    arr2 = sorted([int(i) for i in input().split()])
    res = True
    for i in range(n):
        if(arr1[i] > arr2[i]):
            res = False 
    if(res):
        print("YES")
    else:
        print("NO")