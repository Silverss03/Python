prime = [True] * 1000
prime[0] = prime[1] = False 
for i in range(2, 1000):
    if prime[i] == True :
        for j in range(i * i, 1000, i):
            prime[j] = False
            
for t in range(int(input())):
    num = input()
    if(prime[len(num)] == False):
        print("NO")
    else:
        l = 0
        is_p = not_p = 0 
        while(l < len(num)):
            if(prime[int(num[l])]):
                is_p += 1
            else:
                not_p += 1
            l += 1
        if(is_p > not_p):
            print("YES")
        else:
            print("NO")
    