n, d = [int(i) for i in input().split()]
arr = []
for i in range(n):
    string = input()
    arr.append(string)
res = 0 
idx = 0 
cnt = 0
while idx < d :
    flag = True
    for i in range(n):
        if(arr[i][idx] != 'o'):
            flag = False
            break
    if(flag):
        cnt += 1
        res = max(res, cnt)
    else:
        cnt = 0 
    idx += 1
print(res)
# 3 5
# xooox
# oooxx
# oooxo

# 3 3
# oxo
# oxo
# oxo

# 3 3
# oox
# oxo
# xoo