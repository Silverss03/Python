from datetime import datetime
price = [30, 45, 50, 65, 72, 85, 90, 120, 150]
id_n = 1
class Cus:
    def __init__(self, name_cus, room_n, start, fin, additional) -> None:
        global id_n
        global price
        self.id = "KH" + str(id_n).zfill(2)
        id_n += 1
        self.room_n = room_n
        self.name_cus = name_cus
        floor = int(room_n[0])
        a = datetime.strptime(start, "%d/%m/%Y")
        b = datetime.strptime(fin, "%d/%m/%Y")
        self.days = int((b-a).days) + 1
        self.price = self.days * price[floor - 1] + additional
    
    def __str__(self) -> str:
        return f"{self.id} {self.name_cus} {self.room_n} {self.days} {self.price}"
n = int(input())
ls = []
for i in range(n):
    ls.append(Cus(input(), input(), input(), input(), int(input())))
for i in sorted(ls, key= lambda x : (-x.price, x.days)):
    print(i)