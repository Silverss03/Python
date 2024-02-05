n = input()
res = []
for i in range(0,len(n), 2):
    tmp = n[i:i+2]
    if(len(tmp) == 2 and int(tmp) not in res):
        res.append(int(tmp))
res.sort()
print(*res)