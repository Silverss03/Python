def ex(s):
    res = 0
    for i in range(len(s) - 1, -1 , -1):
        if(s[i] == "1"):
            res += 2**(len(s) - i - 1)
    return str(res)

s = input()
l = len(s) - 1
n = len(s) // 3
res = ""
i = 0
for i in range(n) :
    tmp = ""
    for j in range(3):
        tmp += s[l]
        l -= 1
    res += ex(tmp[::-1])
if(l != -1):
    res += ex(s[:(l+1)])
print(res[::-1])
