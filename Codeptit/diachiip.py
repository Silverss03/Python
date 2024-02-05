for t in range(int(input())):
    ip = input().split(".")
    res = True
    if(len(ip) != 4):
        res = False
    else:            
        for i in range(4):
            if( ip[i].isdigit() == False or int(ip[i]) < 0 or int(ip[i]) > 255 ):
                res = False
    if(res):
        print("YES")
    else:
        print("NO")

# 2
# 192.168.1.1
# 256.255.255.255