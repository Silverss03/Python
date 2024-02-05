from datetime import datetime 
class Guest:
    name = ""
    room = ""
    in_time = ""
    out_time = ""
    price = 0
    id = ""
    days = 0 
    def __init__(self,ID_n, name, room, check_in, check_out, extra):
        self.id = "KH" + str(ID_n).zfill(2)
        self.name = name 
        self.room = room 
        d1 = datetime.strptime(check_in, "%d/%m/%Y")
        d2 = datetime.strptime(check_out, "%d/%m/%Y")
        self.days = abs((d2 - d1).days + 1)
        if(room[0] == "1"):
            self.price = self.days * 25 + extra
        elif(room[0] == "2"):
            self.price = self.days * 34 + extra
        elif(room[0] == "3"):
            self.price = self.days * 50 + extra
        else:
            self.price = self.days * 80 + extra
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.room} {self.days} {self.price}"
        
n = int(input())
arr = []
for i in range(1, n + 1):
    arr.append(Guest(i, input().strip(), input().strip(), input().strip(), input().strip(), int(input())))
for i in sorted(arr, key= lambda x : -x.price):
    print(i)

# 3
# Huynh Van Thanh   
# 103 
# 05/06/2010   
# 05/06/2010   
# 15
# Le Duc Cong  
# 106 
# 08/03/2010   
# 01/05/2010   
# 220
# Tran Thi Bich Tuyen   
# 207 
# 10/04/2010   
# 21/04/2010   
# 96