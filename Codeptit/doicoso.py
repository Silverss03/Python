def change(n, b):
    res = ""
    while(n > 0):
        tmp = n % b 
        n = n // b
        if(tmp < 10):
            res += str(tmp)
        else:
            res += chr(ord('A') + (tmp -10))
    return res[::-1]
for t in range(int(input())):
    n, b = [int(i) for i in input().split()]
    print(change(n,b))
