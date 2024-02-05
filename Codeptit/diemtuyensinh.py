def bonus(ethnic, region):
    bonus_p = 0 
    if(region == "1"):
        bonus_p += 1.5
    elif(region == "2"):
        bonus_p += 1 
    if(ethnic != "Kinh"):
        bonus_p += 1.5
    return bonus_p

def fix(name):
    words = name.split()
    name = ""
    for i in words:
        name += i[0].upper() + i[1:].lower() + " "
    return name

class Student:
    def __init__(self, ID_n, name, bas_point, ethnic, region) :
        self.ID_n = ID_n
        if(ID_n < 100):
            self.ID = 'TS' + str(ID_n).zfill(2)
        else:
            self.ID = 'TS' + str(ID_n).zfill(3)
        self.name = fix(name) 
        self.ethnic = ethnic
        self.region = region
        self.point = float(bas_point) + bonus(self.ethnic, self.region)
        if(self.point >= 20.5):
            self.status = "Do"
        else:
            self.status = "Truot"
    
    def __lt__(self, obj):
        if(self.point != obj.point):
            return self.point < obj.point
        return self.ID_n > obj.ID_n
    
    def __gt__(self, obj):
        if(self.point != obj.point):
            return self.point > obj.point
        return self.ID_n < obj.ID_n
    
    
    def __le__(self, obj):
        if(self.point != obj.point):
            return self.point <= obj.point
        return self.ID_n >= obj.ID_n
    
    def __ge__(self, obj):
        if(self.point != obj.point):
            return self.point >= obj.point
        return self.ID_n <= obj.ID_n
    
    
    def out(self):
        print(self.ID + " " + self.name,end="")
        print("{:.1f}".format(self.point) + " " + self.status)
n = int(input())
res = []
for i in range(1, n + 1):
    name = input().strip()
    basic_p = input()
    ethnic = input()
    region = input()
    stu = Student(i, name, basic_p, ethnic, region)
    res.append(stu)
res = sorted(res, reverse= True)
for i in res:
    i.out()


