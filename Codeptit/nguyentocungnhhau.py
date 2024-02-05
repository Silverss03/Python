import math
n = input()
arr = [int(i) for i in input().split()]
arr = sorted(arr)
for i in range (len(arr)):
    for j in range(i + 1, len(arr)):
        if(math.gcd(arr[i], arr[j]) == 1):
            print(str(arr[i]) + " " + str(arr[j]))
