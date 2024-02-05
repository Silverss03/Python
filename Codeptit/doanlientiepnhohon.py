def top(stack):
    if(len(stack) > 0):
        tmp = stack.pop()
        stack.append(tmp)
    return tmp
for t in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    stack = []
    num = []
    dic = {}
    stack.append(0)
    num.append(1)
    dic[0] = 1
    for i in range(1, n):
        if(arr[i] < arr[top(stack)]):
            dic[i] = 1
        else:
            while(len(stack) > 0 and arr[i] >= arr[top(stack)]):
                tmp = stack.pop()
            if(len(stack) == 0):
                dic[i] = i + 1 
            else:
                dic[i] = (i - tmp+ dic[tmp])
        stack.append(i)            
    for i in range(n):
        print(dic[i], end= " ")
    print()