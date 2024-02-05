for t in range(int(input())):
    n, m, k = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    arr2 = [int(i) for i in input().split()]
    arr3 = [int(i) for i in input().split()]
    res = []
    x = y = z = 0
    while(x < len(arr) and y < len(arr2) and z < len(arr3)):
        if(arr[x] == arr2[y] and arr2[y] == arr3[z]):
            res.append(arr[x])
            x += 1
            y += 1
            z += 1
        elif(arr3[z] <= arr2[y] and arr3[z] <= arr[x]):
            z += 1
        elif(arr2[y] <= arr3[z] and arr2[y] <= arr[x]):
            y += 1
        else:
            x += 1
    if(len(res) > 0):
        print(*res)
    else:
        print("NO")

# 3
# 6 5 8
# 1 5 10 20 40 80
# 5 7 20 80 100
# 3 4 15 20 30 70 80 120
# 3 5 4
# 1 5 5
# 3 4 5 5 10
# 5 5 10 20
# 3 3 3
# 1 2 3
# 4 5 6
# 7 8 9