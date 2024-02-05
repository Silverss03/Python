n = input()
cnt = 0
while(True):
    sum = 0 
    if(n[0] != '-'):
        for i in range(len(n)):
            sum += int(n[i])
        n = str(sum)
    else:
        for i in range(1, len(n)):
            sum += int(n[i])
        n = str(sum)
    cnt += 1
    if(len(n) == 1) or (len(n) == 2 and n[0] == '-'):
        break
print(cnt)