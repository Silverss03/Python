n = input()
k = int(input())
out = False
res = []
cnt = [0] * 100
for i in range(0,len(n), 2):
    tmp = n[i:i+2]
    num = int(tmp)
    if(len(tmp) == 2 ):
        if( num not in res):
            res.append(num)
        cnt[num] += 1
res.sort()
for i in res :
    if(cnt[i] >= k):
        print("{} {}".format(i, cnt[i]))
        out = True
if not out:
    print("NOT FOUND")