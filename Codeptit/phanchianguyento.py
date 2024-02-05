def isPrime(n):
    if(n % 2 == 0 and n != 2):
        return False
    for i in range(3, int(n**0.5) + 1, 2) :
        if(n % i == 0):
            return False 
    return True 

n = int(input())
inp = [int(i) for i in input().split()]
arr = []
for i in inp:
    if i not in arr:
        arr.append(i)
s = sum(arr)
s_l = 0 
idx = 0 
res = False
while(idx < len(arr)):
    s_l += arr[idx]
    s -= arr[idx]
    if(isPrime(s_l) and isPrime(s)):
        res = True
        break
    idx += 1
if(res):
    print(idx)
else:
    print("NOT FOUND")

# 10
# 3 6 7 3 5 7 3 6 6 7
