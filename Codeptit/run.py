id_n = 1
time_ls = []
class Racer:
    def __init__(self, name, b_day, start, fin) -> None:
        global id_n
        global time_ls
        self.id = "VDV" + str(id_n).zfill(2)
        id_n += 1
        arr = name.lower().strip().split()
        s = ""
        for i in arr :
            s += i[0].upper() + i[1:] + " "
        self.name = s.strip()
        y = b_day.split("/")
        age = 2021 - int(y[2])
        secs = int(fin[:2]) * 3600 + int(fin[3:5]) * 60 + int(fin[6:]) - int(start[:2]) * 3600 - int(start[3:5]) * 60 - int(start[6:]) 
        self.real_res = self.to_Time(secs)
        self.rank_time = secs - self.prio(age)
        self.prio_time = self.to_Time(self.prio(age))
        self.prio_res = self.to_Time(self.rank_time)
        time_ls.append(self.rank_time)
    def prio(self, age):
        if age >= 32 :
            return 3
        if age >= 25:
            return 2
        if age >= 18:
            return 1
        else:
            return 0
        
    def set_Rank(self):
        time_ls.sort()
        rank = 1
        for i in time_ls:
            if self.rank_time == i:
                self.rank = rank 
                break
            rank += 1
    
    def to_Time(self, t):
        h = t // 3600
        m = t % 3600 // 60
        s = t % 3600 % 60
        return f"{h:02d}:{m:02d}:{s:02d}" 
    
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.real_res} {self.prio_time} {self.prio_res} {self.rank}"
n = int(input())
ls = []
for i in range(n):
    ls.append(Racer(input(), input(), input(), input()))
for i in ls :
    i.set_Rank()
for i in sorted(ls, key= lambda x : (x.rank)):
    print(i)

# 4
# TRAn TRuNg KiEN
# 8/9/2003
# 07:00:00
# 07:10:01
# DuOnG ANh DUC
# 2/12/2003
# 07:02:00
# 07:11:20
# Nguyen HUU manh
# 10/8/2003
# 07:02:00
# 07:11:20
# TRaN DUc HUy
# 27/4/2003
# 07:05:00
# 07:15:30