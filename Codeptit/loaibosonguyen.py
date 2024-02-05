import sys

with open("DATA.in", "r") as file1:
    res = []
    while True:
        line = file1.readline()
        if not line:
            break
        arr = line.split()
        for i in arr:
            if i.isdigit() == False or int(i) > sys.maxsize:
                res.append(i)
    res = sorted(res)
    for i in res:
        print(i, end=" ")
