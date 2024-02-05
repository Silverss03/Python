a,b,c=map(float,input().split())
if (a+b)>c and (a+c)>b and (b+c)>a:
    if a==b==c:
        print('{},{},{} là 3 cạnh của 1 tam giác đều'.format(a,b,c))
    elif a==b or a==c or b==c:
        print('{},{},{} là 3 cạnh của 1 tam giác cân'.format(a,b,c))
    elif a**2+b**2==c**2 or a**2+c**2==c**2 or b**2+c**2==a**2:
        print('{},{},{} là 3 cạnh của 1 tam giác vuông'.format(a,b,c))
    elif a**2>b**2+c**2 or b**2>a**2+c**2 or c**2>a**2+b**2:
        print('{},{},{} là 3 cạnh của 1 tam giác tù'.format(a,b,c))
    else:
        print('{},{},{} là 3 cạnh của 1 tam giác nhọn'.format(a,b,c))
else:
    print('{},{},{} không phải là 3 cạnh của 1 tam giác'.format(a,b,c))