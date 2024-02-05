def check(n):
    string = n[::-1]
    if(string != n):
        return False
    if(len(n) % 2 != 0):
        return False
    for i in range(len(n)):
        if(int(n[i]) % 2 != 0):
            return False
    return True

for t in range(int(input())):
    n = int(input())
    for i in range(22, n):
        if(check(str(i))):
            print(i, end= " ")
    print()