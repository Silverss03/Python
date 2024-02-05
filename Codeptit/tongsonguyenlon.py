def plus(n1, n2, l, r):
    res = []
    idx = 0
    own = 0
    if(l < r):
        while(idx < l):
            tmp = int(n1[idx]) + int(n2[idx])
            if(own != 0):
                tmp += own 
                own = 0 
            if(tmp >= 10):
                tmp %= 10
                own = 1
            res.insert(0, tmp)
            idx += 1
        while(idx < r):
            tmp = int(n2[idx])
            if(own != 0):
                tmp += own
                own = 0 
            if(tmp >= 10):
                tmp %= 10
                own += 1
            res.insert(0, tmp)
            idx += 1
        if(own != 0):
            res.insert(0, 1)
    else:
        while(idx < r):
            tmp = int(n1[idx]) + int(n2[idx])
            if(own != 0):
                tmp += own 
                own = 0 
            if(tmp >= 10):
                tmp %= 10
                own += 1
            res.insert(0, tmp)
            idx += 1
        while(idx < l):
            tmp = int(n1[idx])
            if(own != 0):
                tmp += own
                own = 0 
            if(tmp >= 10):
                tmp %= 10
                own += 1
            res.insert(0, tmp)
            idx += 1
        if(own != 0):
            res.insert(0, 1)
    return res

n1 = list(input()[::-1])
n2 = list(input()[::-1])
res = plus(n1,n2, len(n1), len(n2))
idx = 0
for i in range(len(res) - 1) :
    if res[i] == 0:
        idx += 1
    else:
        break
for i in range(idx, len(res)):
    print(res[i], end= "")

# 00121212121212121212
# 045678978