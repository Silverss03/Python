n = input()
while(len(n) != 1):
    m = int(len(n)/2)
    a = int(n[:m])
    b = int(n[m:])
    print(a + b)
    n = str(a + b)
