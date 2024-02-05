for i in range(int(input())):
    x, y, z = [int(i) for i in input().split()]
    times = z // (x + y)
    left = z % (x + y)
    if(left < x):
        print(5 * (x * times + left))
    else:
        print(5 * (x * times  + x))