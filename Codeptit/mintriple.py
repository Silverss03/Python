import sys
for t in range(int(input())):
    f_min = s_min = t_min = sys.maxsize
    n = int(input())
    arr = list(map(int, input().split()))
    while(len(arr) > 0):
        if(arr[0] < f_min):
            t_min = s_min
            s_min = f_min
            f_min = arr[0] 
        elif(arr[0] < s_min):
            t_min = s_min
            s_min = arr[0] 
        elif(arr[0]  < t_min):
            t_min = arr[0] 
        arr.remove(arr[0] )
    print(f_min + s_min + t_min)