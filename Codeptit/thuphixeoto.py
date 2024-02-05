time = []
res = []
cnt = 0 
def price(car, seats):
    if(car == "Xe_con"):
        if(seats == 5):
            return 10000
        elif(seats == 7):
            return 15000
    if(car == "Xe_tai" and seats == 2):
        return 20000
    if(car == "Xe_khach"):
        if(seats == 29):
            return 50000
        elif(seats == 45):
            return 70000
for n in range(int(input())):
    info = input().split()
    if(n == 0):
        time.append(info[4])
    if info[4] not in time and n != 0:
        time.append(info[4])
        res.append(cnt)
        cnt = 0 
    if(info[3] == "IN"):
        cnt += price(info[1], int(info[2]))
res.append(cnt)
for i in range(len(time)):
    print(time[i] + ": " + str(res[i]))

# 5
# 30F-123.15 Xe_con 5 OUT 06/11/2021
# 30F-123.15 Xe_con 5 IN 06/11/2021
# 30H-123.15 Xe_con 7 IN 06/11/2021
# 29H-222.68 Xe_tai 2 IN 07/11/2021
# 30G-511.15 Xe_con 5 IN 07/11/2021
