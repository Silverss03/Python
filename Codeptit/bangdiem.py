from decimal import ROUND_HALF_UP, Decimal
class Student:
    def __init__(self, name, points,id_n) :
        self.ID = "HS" + "{:02d}".format(id_n)
        id_n += 1
        self.name = name
        res = 0 
        res = points[0] * 2 + points[1] * 2
        for i in range(2, 10):
            res += points[i]
        res /= 12
        self.point = res.quantize(Decimal('0.1'), ROUND_HALF_UP)
        if(self.point >= 9):
            self.rank = "XUAT SAC"
        elif(self.point >= 8 and self.point <= 8.9):
            self.rank = "GIOI"
        elif(self.point >= 7 and self.point <= 7.9):
            self.rank = "KHA"
        elif(self.point >= 5 and self.point <= 6.9):
            self.rank = "TB"
        else:
            self.rank = "YEU"
    def __lt__ (self, obj):
        if(self.point == obj.point):
            return self.ID < obj.ID
        return self.point > obj.point
    def __gt__ (self, obj):
        if(self.point == obj.point):
            return self.ID > obj.ID
        return self.point < obj.point
    def __le__ (self, obj):
        if(self.point == obj.point):
            return self.ID <= obj.ID
        return self.point >= obj.point
    def __ge__ (self, obj):
        if(self.point == obj.point):
            return self.ID >= obj.ID
        return self.point <= obj.point
    def out(self):
        print(self.ID + " " + self.name + " " + "{:.1f}".format(self.point) + " " + self.rank)
n = int(input())
ls = []
for t in range(n):
    name = input()
    points = [Decimal(i) for i in input().split()]
    tmp = Student(name, points,t + 1)
    ls.append(tmp)
ls = sorted(ls)
for i in range(1, n + 1):
    ls[i - 1].out()
# 4
# Luu Thuy Nhi
# 9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
# Le Van Tam
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Nguyen Thai Binh
# 9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
# Nguyen Huu Manh
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8