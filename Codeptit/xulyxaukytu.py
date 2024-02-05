s1 = input().lower().split()
s2 = input().lower().split()
r1 = []
r2 = []
for i in s1:
    if(i not in r1):
        r1.append(i)
for i in s2:
    if(i not in r1):
        r1.append(i)
r1.sort()
print(*r1)
for i in s1:
    if(i in s2 and i not in r2):
        r2.append(i)
r2.sort()
print(*r2)