for t in range(int(input())):
    mul = 1
    n = input()
    for i in range(len(n)):
        if(n[i] != '0'):
            mul *= int(n[i])
    print(mul)
    