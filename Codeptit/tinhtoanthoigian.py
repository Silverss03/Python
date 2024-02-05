class Gamer:
    minutes = 0 
    id = ""
    name = ""
    def __init__(self, id, name, x, y) :
        self.id = id 
        self.name = name 
        self.minutes = y[0] * 60 + y[1] - x[0] * 60 - x[1]
    def out(self):
        h = int(self.minutes / 60)
        m = self.minutes - 60*h
        print(self.id + " " + self.name + " " + str(h) + " gio " + str(m) + " phut")
    def __lt__(self,object):
        return self.minutes < object.minutes 
    def __gt__(self,object):
        return self.minutes > object.minutes 
    def __le__(self,object):
        return self.minutes <= object.minutes 
    def __ge__(self,object):
        return self.minutes >= object.minutes 
n = int(input())
ls = []
for t in range(n):
    id = input()
    name = input()
    a = [int(i) for i in input().split(":")]
    b = [int(i) for i in input().split(":")]
    ls.append(Gamer(id, name, a, b))
ls = sorted(ls, reverse= True)
for i in range(n):
    ls[i].out()
# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00