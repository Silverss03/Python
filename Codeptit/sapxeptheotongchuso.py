def sum(n):
    res = 0 
    while(n > 0):
        res += n % 10
        n = int(n/10)
    return res

class number:
    def __init__(self, num, s) :
        self.num = num
        self.s = s
    def __lt__(self, obj):
        if(self.s == obj.s):
            return self.num < obj.num
        return (self.s) < (obj.s)
    def __gt__(self, obj):
        if(self.s == obj.s):
            return self.num > obj.num
        return (self.s) > (obj.s) 
    def __le__(self, obj):
        if(self.s == obj.s):
            return self.num <= obj.num
        return (self.s) <= (obj.s) 
    def __ge__(self, obj):
        if(self.s == obj.s):
            return self.num >= obj.num
        return (self.s) >= (obj.s) 
for t in range(int(input())):
    n = input()
    dict = {}
    num = []
    arr = [int(i) for i in input().split()]
    for i in range(len(arr)):
        a = number(arr[i], sum(arr[i]))
        num.append(a)
    num = sorted(num)
    for i in num :
        print(i.num,end= " ")
    print()
    