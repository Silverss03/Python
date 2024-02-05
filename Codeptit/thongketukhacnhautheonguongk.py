import re
class out:
    def __init__(self, a, i) :
        self.word = a 
        self.num = i 
    def __lt__(self, obj):
        if(self.num != obj.num):
            return self.num > obj.num
        return self.word < obj.word
    def __gt__(self, obj):
        if(self.num != obj.num):
            return self.num < obj.num
        return self.word > obj.word
    def __le__(self, obj):
        if(self.num != obj.num):
            return self.num >= obj.num
        return self.word <= obj.word
    def __ge__(self, obj):
        if(self.num != obj.num):
            return self.num <= obj.num
        return self.word >= obj.word
    def __str__(self) -> str:
        return "{} {}".format(self.word, self.num)
n, k = [int(i) for i in input().split()]
string = ""
for i in range(n):
    string += input().lower() + " "
arr = re.findall("[\w]+", string)
mp = {}
for i in arr:
    if i in mp :
        tmp = mp[i]
        mp[i] = tmp + 1
    else:
        mp[i] = 1
ls = []
for i in mp:
    ls.append(out(i, mp[i]))
ls.sort()
for i in ls:
    if(i.word >= k):
        print(i)

# 3 2
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.