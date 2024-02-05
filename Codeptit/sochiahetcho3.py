for t in range(int(input())):
    sum = 0 
    n = input()
    for i in range(len(n)):
        sum += int(n[i])
    if(sum % 3 == 0):
        print("YES")
    else:
        print("NO")
    