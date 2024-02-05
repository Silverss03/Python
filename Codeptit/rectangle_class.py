class Rectangle:
    def __init__(self,a,b,c) :
        self.len = a 
        self.wid = b 
        self.col = c 
    def perimeter(self):
        return((self.len + self.wid) * 2) 
    def area(self):
        return(self.len*self.wid)
    def color(self):
        res = self.col.capitalize()
        return res

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))