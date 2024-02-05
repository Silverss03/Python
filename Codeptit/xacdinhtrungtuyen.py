id_n = 1
class Teacher:
    name = ""
    id = ""
    subject = ""
    total = 0 
    status = ""
    def __init__(self, name, id, it, prof) -> None:
        global id_n
        self.id = "GV" + "{:02d}".format(id_n) 
        id_n += 1
        self.name = name
        if(id[0] == "A"):
            self.subject = "TOAN"
        elif(id[0] == "B"):
            self.subject = "LY"
        else:
            self.subject = "HOA"
        self.total += (it * 2 + prof)
        if(id[1] == "1"):
            self.total += 2
        elif(id[1] == "2"):
            self.total += 1.5
        elif(id[1] == "3"):
            self.total += 1
        if(self.total >= 18):
            self.status = "TRUNG TUYEN" 
        else:
            self.status = "LOAI"
    
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.subject} {self.total} {self.status}"
n = int(input())
ls = []
for i in range(n):
    ls.append(Teacher(input(), input(), float(input()), float(input())))
for i in sorted(ls, key= lambda x : -x.total):
    print(i)

# 3
# Le Van Binh
# A1
# 7.0
# 3.0
# Tran Van Toan
# B3
# 4.0
# 7.0
# Hoang Thi Tam
# C2
# 7.0
# 6.0