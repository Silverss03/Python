n = int(input())
if(n <= 6):
    print(f"{7 - n} {6 * n}")
else:
    times = n // 6
    low = times + (7 - n % 6)
    high = 6 * n
    print(f"{low} {high}")