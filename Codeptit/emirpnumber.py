def isprime(n):
    if(n < 2):
        return False
    for i in range(2, (int)(n**0.5) + 1):
        if(n % i == 0):
            return False
    return True

for t in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        if(isprime(i)):
            reverse = int(str(i)[::-1])
            if(reverse < n and i != reverse and isprime(reverse) and reverse not in arr):
                arr.append(i)
                arr.append(reverse)
    for i in arr :
        print(i, end= " ")
    print()
