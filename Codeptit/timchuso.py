import math
for t in range(1, int(input()) + 1):
    n = int(input())
    res = str(pow(3 + math.sqrt(5), n))
    idx = res.find(".")
    print("Case #" + str(t) + ":", end= " ")
    if(idx >= 3):
        print(res[idx -3 : idx])
    else:
        print(res[:idx].zfill(3))
