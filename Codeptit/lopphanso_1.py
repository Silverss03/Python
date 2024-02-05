import math
a, b = [int(i) for i in input().split()]
c = math.gcd(a,b)
a = int(a/c) 
b = int(b/c)
print(str(a) + "/" + str(b)) 