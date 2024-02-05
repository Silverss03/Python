class Gamer:
    user_name = ""
    pass_word = ""
    name = ""
    h = 0
    m = 0 
    total = 0
    def __init__(self, username, password, name, start, fin) -> None:
        self.user_name = username
        self.pass_word = password
        self.name = name
        self.total= int(fin[:2]) * 60 + int(fin[3:]) - int(start[:2]) * 60 - int(start[3:])
        self.h = self.total // 60 
        self.m = self.total % 60
    def __str__(self) -> str:
        return f"{self.user_name} {self.pass_word} {self.name} {self.h} gio {self.m} phut"

n = int(input())
ls = []
for i in range(n):
    ls.append(Gamer(input(), input(), input(), input(), input()))

for i in sorted(ls, key= lambda x : (-x.total, x.user_name)):
    print(i)

# 5
# anhtuanvip
# 123
# Nguyen Van Tuan
# 05:18
# 07:06
# chickenzero
# 124
# Nguyen Van Phuc
# 05:38
# 14:19
# anhhung123
# matkhau
# Nguyen Manh Hung
# 06:58
# 14:18
# loveyou
# acb
# Luong Van Manh
# 02:01
# 06:47
# taikhoan123
# matkhaumanh
# Nguyen Thi Uyen
# 00:09
# 06:19