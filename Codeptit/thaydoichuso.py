tests = int(input())
while(tests > 0):
    p,q = input().split()
    inp = input().split()
    if(len(inp) == 1):
        num_1 = inp[0] 
        num_2 = input()
    else:
        num_1, num_2 = inp
    a = int(num_1.replace(p,q)) + int(num_2.replace(p,q))
    b = int(num_1.replace(q,p)) + int(num_2.replace(q,p))
    print(str(min(a,b)) + " " + str(max(a,b)))
    tests-=1 

        
