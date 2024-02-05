import math
def score(n):
    if(n >= 39 and n <= 40):
        return 9.0
    if(n >= 37 and n <= 38):
        return 8.5
    if(n >= 35 and n <= 36):
        return 8.0
    if(n >= 33 and n <= 34):
        return 7.5
    if(n >= 30 and n <= 32):
        return 7
    if(n >= 27 and n <= 29):
        return 6.5
    if(n >= 23 and n <= 26):
        return 6
    if(n >= 20 and n <= 22):
        return 5.5
    if(n >= 16 and n <= 19):
        return 5
    if(n >= 13 and n <= 15):
        return 4.5
    if(n >= 10 and n <= 12):
        return 4
    if(n >= 7 and n <= 9):
        return 3.5
    if(n >= 5 and n <= 6):
        return 3.0
    elif(n >= 3 and n <= 4):
        return 2.5
    
for t in range(int(input())):
    r, l, s, w = [float(i) for i in input().split()]
    r = score(r)
    l = score(l)
    point_f = (r + l + s +  w)/4
    point_i = int((r + l + s +  w)/4)
    if(point_f - point_i >= 0.75):
        print(point_i + 1.0)
    elif(point_f - point_i >= 0.25):
        print(point_i + 0.5)
    else:
        print(point_i)
    

# 2
# 15 25 5.0 5.5
# 22 32 6.0 6.0