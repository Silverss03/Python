class Product:
    id = ""
    name = ""
    amount = 0 
    price = 0 
    discount = 0 
    total = 0 
    def __init__(self, id, name, buy, price, discount) -> None:
        self.id = id 
        self.name = name
        self.amount = buy 
        self.price = price 
        self.discount = discount
        self.total = self.price * self.amount - self.discount
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.amount} {self.price} {self.discount} {self.total}"
    
n = int(input())
ls = []
for i in range(n):
    ls.append(Product(input().strip(), input().strip(), int(input()), int(input()), int(input())))
for i in sorted(ls, key= lambda x : -x.total):
    print(i)

# 3
# ML01
# May lanh SANYO
# 12
# 4000000
# 2400000
# ML02
# May lanh HITACHI
# 4
# 2550000000
# 0
# ML03
# May lanh NATIONAL
# 5
# 3000000
# 150000