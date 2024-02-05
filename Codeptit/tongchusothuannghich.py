for t in range(int(input())):
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if(len(str(sum)) > 1 and str(sum) == str(sum)[::-1]):
        print("YES")
    else:
        print("NO")