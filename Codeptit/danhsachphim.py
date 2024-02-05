mp = {}
class phim:
    ma_tl = ""
    ngay = ""
    ten_p = ""
    s_tap = 0
    type = ""
    def __init__(self, ID_n, ma_tl, ngay, ten_p, s_tap) :
        self.ID = 'P' + str(ID_n).zfill(3)
        self.type = mp[ma_tl]
        self.ngay = ngay
        self.ten_p = ten_p 
        self.s_tap = s_tap
    def __lt__ (self, obj):
        if(self.ngay == obj.ngay):
            if(self.ten_p == obj.ten_p):
                return(self.s_tap < obj.s_tap)
            else:
                return(self.ten_p < obj.ten_p)
        else:
            day_a = int(self.ngay[:2])
            month_a = int(self.ngay[3:5])
            year_a = int(self.ngay[6:])
            day_b = int(obj.ngay[:2])
            month_b = int(obj.ngay[3:5])
            year_b = int(obj.ngay[6:])
            if(year_a == year_b):
                if(month_a == month_b):
                    return day_a < day_b
                else:
                    return month_a < month_b
            else:
                return year_a < year_b
    def __gt__ (self, obj):
        if(self.ngay == obj.ngay):
            if(self.ten_p == obj.ten_p):
                return(self.s_tap > obj.s_tap)
            else:
                return(self.ten_p > obj.ten_p)
        else:
            day_a = int(self.ngay[:2])
            month_a = int(self.ngay[3:5])
            year_a = int(self.ngay[6:])
            day_b = int(obj.ngay[:2])
            month_b = int(obj.ngay[3:5])
            year_b = int(obj.ngay[6:])
            if(year_a == year_b):
                if(month_a == month_b):
                    return day_a > day_b
                else:
                    return month_a > month_b
            else:
                return year_a > year_b
    def __le__ (self, obj):
        if(self.ngay == obj.ngay):
            if(self.ten_p == obj.ten_p):
                return(self.s_tap <= obj.s_tap)
            else:
                return(self.ten_p <= obj.ten_p)
        else:
            day_a = int(self.ngay[:2])
            month_a = int(self.ngay[3:5])
            year_a = int(self.ngay[6:])
            day_b = int(obj.ngay[:2])
            month_b = int(obj.ngay[3:5])
            year_b = int(obj.ngay[6:])
            if(year_a == year_b):
                if(month_a == month_b):
                    return day_a <= day_b
                else:
                    return month_a <= month_b
            else:
                return year_a <= year_b
    def __ge__ (self, obj):
        if(self.ngay == obj.ngay):
            if(self.ten_p == obj.ten_p):
                return(self.s_tap >= obj.s_tap)
            else:
                return(self.ten_p >= obj.ten_p)
        else:
            day_a = int(self.ngay[:2])
            month_a = int(self.ngay[3:5])
            year_a = int(self.ngay[6:])
            day_b = int(obj.ngay[:2])
            month_b = int(obj.ngay[3:5])
            year_b = int(obj.ngay[6:])
            if(year_a == year_b):
                if(month_a == month_b):
                    return day_a >= day_b
                else:
                    return month_a >= month_b
            else:
                return year_a >= year_b
    def __str__(self):
        return self.ID + " " + self.type + " " + self.ngay + " " + self.ten_p + " " + str(self.s_tap)
n, m = [int(i) for i in input().split()] 
type = []
ls = []
for i in range(1, n + 1):
    name = input()
    id = "TL" + str(i).zfill(3)
    mp[id] = name
for i in range(1, m + 1):
    type_id = input()
    date = input()
    name = input()
    ep = int(input())
    a = phim(i, type_id, date, name, ep)
    ls.append(a)
ls.sort()
for i in ls:
    print(i)
# 2 3
# Hai huoc
# Tinh cam
# TL001
# 25/11/2021
# Phim so 1
# 10
# TL001
# 04/12/2021
# Phim so 2
# 15
# TL002
# 25/11/2021
# Phim so 3
# 5