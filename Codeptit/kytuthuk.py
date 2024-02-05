def count(n, k):
	x = pow(2,n - 1) 
	if(k == x): return chr(ord('A') + (n - 1) )
	if(k < x): return count(n - 1,k) 
	return count(n-1,k-x) 

for t in range(int(input())):
    n, k = [int(i) for i in input().split()]
    print(count(n,k))

