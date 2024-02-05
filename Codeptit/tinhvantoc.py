class Racer:
    id = ""
    name = ""
    group = ""
    h = 0 
    m = 0 
    speed = 0
    def __init__(self, name, city, time) -> None:
        arr = city.split(" ")
        for i in arr :
            self.id += i[0]
        arr = name.split(" ")
        for i in arr :
            self.id += i[0]
        self.name = name
        self.group = city
        self.time = int(time[:1]) - 6 + (int(time[2:]))/60
        self.speed = round(120 / self.time)
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.group} {self.speed} Km/h"
n = int(input())
ls = []
for i in range(n):
    ls.append(Racer(input(), input(), input()))
for i in sorted(ls, key= lambda x : x.time):
    print(i)

# 3
# Tran Vu Minh
# Ha Noi
# 8:30
# Vu Ngoc Hoang
# Hoa Binh
# 8:20
# Pham Dinh Tan
# An Giang
# 8:45