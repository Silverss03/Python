def isPrime(n):
    if(n % 2 == 0 and n != 2):
        return False
    for i in range(3, int(n**0.5) + 1, 2) :
        if(n % i == 0):
            return False 
    return True 

n = input()
arr = [int(i) for i in input().split()]
prime = []
idx = 0 
for i in arr :
    if(isPrime(i)):
        prime.append(i)
prime.sort()
for i in arr :
    if(isPrime(i)):
        print(prime[idx], end= " ")
        idx += 1
    else:
        print(i, end= " ")

# 8
# 4 6 3 8 7 2 5 9