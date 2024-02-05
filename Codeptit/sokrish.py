def count(n):
    res = 1 
    for i in range(1,n + 1):
        res *= i
    return res 

for t in range(int(input())):
    n = int(input())
    sum = 0 
    tmp = n
    while(tmp > 0):
        sum += count(tmp%10)
        tmp = int(tmp /10) 
    if(n == sum):
        print("Yes")
    else:
        print("No")
