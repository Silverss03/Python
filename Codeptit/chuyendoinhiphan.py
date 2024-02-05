def change(string, b):
    res = ""
    octal = 0 
    for i in range(len(string) - 1, -1, -1):
        if(string[i] == '1'):
            octal += pow(2,len(string) - i - 1)
    if(b == 2):
        return string
    else:
        if(b == 16):
            while(octal > 0):
                octal, remainder = divmod(octal, b)
                if(remainder < 10):
                    res += str(remainder)
                else:
                    res += chr(ord('A') + (remainder - 10))
        else:
            while(octal > 0):
                octal, remainder = divmod(octal, b)
                res += str(remainder)
        return res[::-1]
with open ("DATA.in", "r") as file1:
    times = int(file1.readline())
    for t in range(times):
        b = int(file1.readline())
        string = file1.readline().replace("\n", "")
        print(change(string, b))
file1.close()

    