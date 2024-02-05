import math

class Point:
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def distance(self, object):
        a = self.x - object.x
        b = self.y - object.y
        return math.sqrt(a*a + b*b)
    
class Triangle:
    def __init__(self,x,y,z) :
        self.x = x
        self.y = y 
        self.z = z 
    def cnt(self):
        AB = self.x.distance(self.y)
        BC = self.y.distance(self.z)
        AC = self.x.distance(self.z)
        if(max(AB, BC, AC) * 2 < AB + BC + AC):
            res = math.sqrt((AB + BC + AC) * (AB + BC - AC) * (AB -BC + AC) * (-AB + BC + AC))/4 
            print("{:.2f}".format(res))
        else:
            print("INVALID")
list = []
tests = int(input())
for t in range(tests):
    list += [float(i) for i in input().split()]
i = 0
for index in range(tests):
    triangle = Triangle(Point(list[i], list[i + 1]), Point(list[i + 2], list[i + 3]), Point(list[i + 4], list[i + 5]))
    triangle.cnt()
    i += 6