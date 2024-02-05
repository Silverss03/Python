import math
class fraction:
    def __init__(self,a,b):
        self.num = a
        self.denum = b 
        c = math.gcd(self.num,self.denum)
        self.num = int(self.num/c) 
        self.denum = int(self.denum/c)

    def add(self, object):
        new_d = int((self.denum * object.denum)/math.gcd(self.denum, object.denum))
        mul = int(new_d/self.denum)
        self.num *= mul
        mul = int(new_d/object.denum)
        object.num *= mul
        res = fraction(self.num+object.num, new_d)
        return res
    def out(self):
        print(str(self.num) + "/" + str(self.denum))
a,b,c,d = [int(i) for i in input().split()]
f1 = fraction(a,b)
f2 = fraction(c,d)
f3 = f1.add(f2)
f3.out()