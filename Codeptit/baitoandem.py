n = int(input())
arr = []
miss = 1 
flag = True
while(len(arr) < n):
    arr += [int(i) for i in input().split()]
lim = max(arr)
while(miss <= lim):
    if(miss not in arr):
        print(miss)
        miss += 1
        flag = False
    else:
        miss += 1
if(flag):
    print("Excellent!")