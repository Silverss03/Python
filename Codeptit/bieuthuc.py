for t in range(int(input())):
    s = input()
    q1 = []
    cnt = 1
    for i in s:
        if(i == '('):
            q1.append(cnt)
            print(cnt, end= " ")
            cnt += 1 
        elif(i == ')'):
            print(q1.pop(), end = " ")
    print()