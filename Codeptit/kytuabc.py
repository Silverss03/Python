def act(s, n, a, b, c):
    if(len(s) == n and a > 0 and a <= b and b <= c):
        print(s)
        return
    elif(len(s) < n):
        act(s + 'A', n, a + 1, b, c)
        act(s + 'B', n, a, b + 1, c) 
        act(s + 'C', n, a, b, c + 1)
    return
n = int(input())
for i in range(3, n + 1):
    act('', i,0,0,0)