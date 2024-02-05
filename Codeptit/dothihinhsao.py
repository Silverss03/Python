n =  int(input())
check = [0] * 1002 
List = [[] for _ in range (n + 1)]
for i in range(n - 1):
    x, y = [int(i) for i in input().split()]
    List[x].append(y)
    List[y].append(x)
cnt_1 = 0
cnt_n = 0
for i in range(1, n + 1):
    if(len(List[i]) == 1):
        cnt_1 += 1
    elif (len(List[i]) == n - 1):
        cnt_n += 1
if(cnt_1 == (n - 1) and cnt_n == 1):
    print("Yes")
else:
    print("No")
