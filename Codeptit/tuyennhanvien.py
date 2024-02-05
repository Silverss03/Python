class Candidate:
    def __init__(self, name, id, res) :
        global id_n
        self.id = id
        self.name = name
        self.res = res
        if(self.res < 5):
            self.status = "TRUOT"
        elif(self.res < 8):
            self.status = "CAN NHAC"
        elif(self.res <= 9.5):
            self.status = "DAT"
        else:
            self.status = "XUAT SAC"
    def out(self):
        print(self.id + " " + self.name + " " + "{:.2f}".format(self.res) + " " + self.status)
    def __lt__(self, obj):
        return self.res < obj.res
    def __gt__(self, obj):
        return self.res > obj.res
    def __le__(self, obj):
        return self.res <= obj.res
    def __ge__(self, obj):
        return self.res >= obj.res
n = int(input())
ls = []
for i in range(n):
    name = input()
    theory = float(input())
    practice = float(input())
    theory /= 10 if theory > 10 else 1
    practice /= 10 if practice > 10 else 1
    id = "TS0{}".format(i + 1)
    score = (theory + practice)/2
    ls.append(Candidate(name, id, score))
ls = sorted(ls, reverse = True)
for i in range(n):
    ls[i].out()

# 3
# Nguyen Thai Binh
# 45
# 75
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56