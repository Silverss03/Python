num = input()
n = len(num)
res = True
for i in range(n):
    if(num[i] != '6' and num[i] != '8'):
        res = False
    if(i < n - 1 and num[i] == '6' and (num[i + 1] != '8' and num[i + 1] != '6' )):
        res = False 
    if(i < n - 2 and num[i] == '8' and (num[i + 1] == '8' and num[i + 2] == '8')):
        res = False
if(res):
    print("YES")
else:
    print("NO")