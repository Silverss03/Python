n = int(input())
arr = [int(i) for i in input().split()]

for i in range(1, n + 2):
    if i not in arr:
        print(i)
        break