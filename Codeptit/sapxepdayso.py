import math
for t in range(int(input())):
    n, m = [int(i) for i in input().split()]
    ls = [int(i) for i in input().split()]
    ge = max(ls)
    neg = []
    re = []
    for i in range(len(ls)):
        if(ls[i] == ge):
            ls.insert(i, m)
            break
    for i in range(len(ls)):
        if(ls[i] < 0):
            neg.append(ls[i])
        else:
            re.append(ls[i])
    for i in neg :
        print(i, end= " ")
    for i in re :
        print(i, end= " ")
    print()    

    