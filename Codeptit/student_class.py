class Student:
    def __init__(self, name, date, num1, num2, num3) :
        self.name = name 
        self.date = date
        self.point = num1 + num2 + num3
    def out(self):
        print(self.name + " " + self.date + " " + "{:.1f}".format(self.point))

name = input()
date = input()
n1 = float(input())
n2 = float(input())
n3 = float(input())
s = Student(name, date, n1, n2, n3)
s.out()