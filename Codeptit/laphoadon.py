id_n = 1 
class Customer:
    name = ""
    ID = ""
    price = 0 
    def __init__(self, name, old_idx, new_idx) :
        global id_n 
        self.name = name
        diff = new_idx - old_idx
        if diff <= 50:
            self.price = diff * 1.02 *100
        elif diff <= 100 :
            self.price = (50 * 100 + (diff - 50) * 150) * 1.03
        else:
            self.price = (50 * 100 + 50 * 150 + (diff - 100) * 200) * 1.05
        self.price = round(self.price)
        self.ID = "KH" + "{:02d}".format(id_n)
        id_n += 1
    def __lt__(self, obj):
        return self.price > obj.price 
    def __gt__(self, obj):
        return self.price < obj.price 
    def __le__(self, obj):
        return self.price >= obj.price 
    def __ge__(self, obj):
        return self.price <= obj.price
    def out(self):
        print(self.ID + " " + self.name + " " + str(self.price))
n = int(input())
ls = []
for t in range(n):
    name = input()
    s = int(input())
    e = int(input())
    tmp = Customer(name, s, e)
    ls.append(tmp)
ls = sorted(ls)
for i in ls :
    i.out()

# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612