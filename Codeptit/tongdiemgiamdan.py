id_n = 1
class Student:
    def __init__(self, name, b_day, s_1, s_2, s_3 ) -> None:
        global id_n
        self.id = id_n
        id_n += 1
        self.name = name
        self.b_day = b_day
        self.score = s_1 + s_2 + s_3
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.b_day} {self.score:.1f}"
ls = []
n = int(input())
for i in range(n):
    ls.append(Student(input(), input(), float(input()), float(input()) , float(input())))
ls.sort( key= lambda x : (-x.score, x.id))
for i in ls:
    print(i)