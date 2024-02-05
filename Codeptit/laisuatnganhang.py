for t in range(int(input())):
    n, x, m = [float(i) for i in input().split()]
    x = float(x/100)
    years = 0
    while(n < m):
        income = float(x * n) 
        n += income
        years+=1
    print(years)