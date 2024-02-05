def time(x,y):
    return y[0] * 60 + y[1] - x[0] * 60 - x[1]
stations = []
info = {}
n = int(input())
for i in range(n):
    name = input()
    start = [int(j) for j in input().split(':')]
    end = [int(j) for j in input().split(':')]
    amount = int(input())
    if(name not in stations):
        stations.append(name)
        info[name] = (time(start,end), amount)
    else:
        info[name] = (info[name][0] + time(start,end) , info[name][1] + amount)
num = 1
for i in stations:
    print("T{:02d}".format(num) + " " + i + " " + "{:.2f}".format(info[i][1] * 60 /info[i][0]))
    num+=1
# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35