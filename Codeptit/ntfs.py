n = int(input()) 
res = 0 
while(True):
    if(n > 0):
        res += 1
    else:
        break
    n -= (1024) * 4
print(res * 4)