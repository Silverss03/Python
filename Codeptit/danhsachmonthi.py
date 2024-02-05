class Subject:
    id = ""
    name = ""
    form = ""
    def __init__(self, id, name, form):
        self.name = name
        self.form = form
        self.id = id
    def __str__(self):
        return f"{self.id} {self.name} {self.form}"

n = int(input())
arr = []
for i in range(n):
    arr.append(Subject(input(), input(), input()))
for i in sorted(arr, key=lambda x : x.id):
    print(i)

# 2
# MUL1320
# Nhap mon da phuong tien
# Bai tap lon + Van dap truc tuyen
# BAS1203
# Giai tich 1
# Thi viet + Van dap truc tuyen