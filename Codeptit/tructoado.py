class pair :
    s = 0 
    e = 0
    def __init__(self, s, e) :
        self.s = s 
        self.e = e
    def __lt__(self, obj):
        return self.e < obj.e
    def __gt__(self, obj):
        return self.e > obj.e
    def __le__(self, obj):
        return self.e <= obj.e
    def __ge__(self, obj):
        return self.e >= obj.e
    
for t in range(int(input())):
    ls = []
    cnt = 1
    n = int(input())
    for i in range(n):
        s, e = [int(i) for i in input().split()]
        ls.append(pair(s, e))
    ls.sort()
    curr = ls[0].e
    for i in range(1, len(ls)):
        if(ls[i].s >= curr):
            cnt += 1
            curr = ls[i].e
    print(cnt)


# 1
# 10
# 39 55
# 37 74
# 0 1
# 19 25
# 65 76
# 51 52
# 19 21
# 5 94
# 46 65
# 32 40