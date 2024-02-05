proto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while((inp := input()) != "0"):
    res = ""
    decode = inp.split()
    num = int(decode[0])
    string = decode[1]
    for i in range(len(string)):
        pos = proto.find(string[i]) 
        pos += num 
        if(pos > 27):
            pos -= 28
        res += proto[pos]
    print(res[::-1])
