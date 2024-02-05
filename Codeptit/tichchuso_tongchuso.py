for t in range(int(input())):
    num = input()
    sum = 0 
    mul = 1 
    ok = 0
    for i in range(len(num)):
        if(i % 2 != 0):
            sum += int(num[i])
        else:
            if(num[i] != '0'):
                mul *= int(num[i])
                ok = 1
    if(ok == 0): mul = 0
    print(str(mul) + " " + str(sum))