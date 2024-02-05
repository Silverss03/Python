n = input()
res = []
cnt = [0] * 100
for i in range(0,len(n), 2):
    tmp = n[i:i+2]
    num = int(tmp)
    if(len(tmp) == 2 ):
        if( num not in res):
            res.append(num)
        cnt[num] += 1
for i in res :
    print("{} {}".format(i, cnt[i]))