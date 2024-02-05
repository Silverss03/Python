arr = input().split()
res = ""
for i in arr :
    res += i[0].upper() + i[1:]
print(res)