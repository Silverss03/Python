def sal_mul(ID):
    team = ID[0]
    year = int(ID[1:3])
    if(year >= 1 and year <= 3):
        if(team == "A"):
            return 10
        elif(team == "B"):
            return 10
        elif(team == "C"):
            return 9
        else:
            return 8
    elif(year >= 4 and year <= 8):
        if(team == "A"):
            return 12
        elif(team == "B"):
            return 11
        elif(team == "C"):
            return 10
        else:
            return 9
    elif(year >= 9 and year <= 15):
        if(team == "A"):
            return 14
        elif(team == "B"):
            return 13
        elif(team == "C"):
            return 12
        else:
            return 11
    else:
        if(team == "A"):
            return 20
        elif(team == "B"):
            return 16
        elif(team == "C"):
            return 14
        else:
            return 13     
        
n = int(input())
list = {}
res = []
for i in range(n):
    inp = input()
    list[inp[0:2]] = inp[3:]

class employee:
    def __init__(self, ID, name, days , bas_sal):
        self.ID = ID 
        self.name = name 
        self.days = int(days)
        self.bas_sal = int(bas_sal)
        self.sal = sal_mul(self.ID) * self.bas_sal * self.days
        self.team = ID[3:]
    def out(self):
        print(str(self.ID) + " " + str(self.name) + " " + list[self.team] + " " + str(self.sal) + "000")

n = int(input())
for i in range(n):
    ID = input().strip()
    name = input()
    day = input()
    bas_sal = input()
    emp = employee(ID, name, day, bas_sal)
    res.append(emp)
for i in res:
    i.out()

