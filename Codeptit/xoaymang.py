for t in range(int(input())):
    inp = input().split() 
    n, d = int(inp[0]), int(inp[1])
    arr = [int(i) for i in input().split()]
    for i in range(d, n):
        print(arr[i], end= " ")
    for i in range(0, d):
        print(arr[i], end= " ")
    print()