class Student:
    id = ""
    name = ""
    group = ""
    point = 10 
    status = ""
    def __init__(self, id, name, group) :
        self.id = id 
        self.name = name
        self.group = group
    def count(self, check):
        self.point = self.point - check.count("v")*2 - check.count("m") 
        if(self.point <= 0):
            self.point = 0
            self.status = "0 KDDK"
        else:
            self.status += str(self.point)
    def __str__(self):
        return f"{self.id} {self.name} {self.group} {self.status}"

n = int(input())
ls = []
for i in range(n):
    id = input()
    name = input()
    group = input()
    ls.append(Student(id, name, group))
for i in range(n):
    id, check = input().split()
    for j in range(len(ls)):
        if(ls[j].id == id):
            ls[j].count(check)
for i in range(n):
    print(ls[i])
# 3
# B19DCCN999
# Le Cong Minh
# D19CQAT02-B
# B19DCCN998
# Tran Truong Giang
# D19CQAT02-B
# B19DCCN997
# Nguyen Tuan Anh
# D19CQCN04-B
# B19DCCN998 xxxmxmmvmx
# B19DCCN997 xmxmxxxvxx
# B19DCCN999 xvxmxmmvvm