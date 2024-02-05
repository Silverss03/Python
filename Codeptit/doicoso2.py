proto = '0123456789ABCDEF'
def convert(string):
    s = string[::-1]
    res = 0
    for i in range(0, len(s)):
        if s[i] == '1':
            res += 2 ** i 
    return res
def act(string, base):
    global proto
    res = ""
    s_10 = convert(string)
    if base == 2:
        return string
    elif base == 4 :
        while s_10 > 0 :
            res += str(s_10 % 4)
            s_10 = s_10 // 4
    elif base == 8 : 
        while s_10 > 0 :
            res += str(s_10 % 8)
            s_10 = s_10 // 8 
    elif base == 16:
        while s_10 > 0 :
            res += proto[s_10 % 16]
            s_10 = s_10 // 16
    return res[::-1]
for t in range(int(input())):
    base = int(input())
    string = input()
    print(act(string, base))


# 3
# 8
# 10010100010010101
# 2
# 10010100010010101
# 16
# 1010000100100001101111001101
