arr = list()
N = 10**18

i =  1 

while i <= N :
    j = 1
    while j <= N:
        k = 1
        while k <= N:
            arr += [i*j*k]
            k *= 5
        j *= 3
    i *= 2

arr.sort()          

def bin_search(n , l , r):
    if(l > r):
        print("Not in sequence")
        return
    mid = int((l + r)/ 2) 
    if(arr[mid] == n):
        print( mid + 1 )
    elif(arr[mid] > n):
        return bin_search(n, l, mid - 1)
    else:
        return bin_search(n, mid + 1, r)
      
for t in range(int(input())):
    n = int(input())
    bin_search(n, 0, len(arr) - 1)