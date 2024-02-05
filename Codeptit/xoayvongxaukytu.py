n = int(input())
ls = []
for i in range(n):
    ls.append(input())
s, ok, ans = ls[0], 1, 100
m = len(s)
for i in range(m):
    cnt = 0 
    for j in range(n):
        tmp = ls[j]
        for k in range(m):
            if tmp == s:
                cnt += k
                break
            else:
                tmp = tmp[1::] + tmp[0]
        if(tmp != s):
            ok = 0
    ans = min(cnt, ans)
    s = s[1::] + s[0]
if(ok == 1):
    print(ans)
else:
    print(-1)
# 3
# aa
# aa
# ab