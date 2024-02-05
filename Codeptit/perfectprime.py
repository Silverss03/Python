tests = int(input())
from math import sqrt

def is_prime(n):
    if(n < 2): return False
    for i in range (2, int(sqrt(n))):
        if(n % i == 0): return False
    return True 

while tests > 0:
    n = int(input())
    reverse = 0 
    number = True
    sum = 0
    if(is_prime(n)):
        while(n > 0):
            tmp = n % 10 
            sum +=  tmp 
            if(is_prime(tmp) == False):
               number = False
               break
            else: 
                reverse = reverse * 10 + tmp
            n = int(n/10) 
        if(is_prime(sum) and is_prime(reverse) and number):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
    tests -= 1