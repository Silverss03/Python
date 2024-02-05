for t in range(0,int(input())):
    n=int(input())
    a=[int(k) for k in input().split()]
    mx=[0]*n
    mn=[0]*n
    mx[0]=-1
    mn[n-1]=10000000000000
    for i in range(1,n):
        mx[i]=max(a[i-1],mx[i-1])
    for i in range(n-2,-1,-1):
        mn[i]=min(a[i+1],mn[i+1])
    cnt=0
    for i in range(0,n):
        if a[i]>=mx[i] and a[i]<mn[i]:
            cnt+=1
    print(cnt)