num = input()
res = ""
for i in range(-1, -len(num) - 1, -1):
    res += num[i] 
    if(i % 3 == 0 and i != -len(num)):
        res += ","
print(res[::-1])