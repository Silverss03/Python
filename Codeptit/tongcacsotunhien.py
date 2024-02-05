def act(lim,i,remain):
    for j in range(lim , 0, -1):
        arr[i] = j
        if(j == remain):
            string = "("
            for k in range(1, i):
                string += str(arr[k]) + " "
            string += "{})".format(arr[i]) 
            res.append(string)
        elif(j < remain):
            act(j, i + 1, remain - j)
for t in range(int(input())):
    res = []
    n = int(input())
    arr = [0] * (n + 1)
    act(n,1,n)
    print(len(res))
    print(*res, sep= " ")