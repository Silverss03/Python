n = int(input())
arr = []
while(True):
    if(n == 0):
        break
    arr  += [int(i) for i in input().split()]
    n -= (len(arr))
even = []
idx_even = 0
odd = []
idx_odd = 0
for i in arr :
    if i % 2 == 0 :
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort(reverse= True)
for i in arr :
    if(i % 2 == 0):
        print(even[idx_even], end= " ")
        idx_even += 1
    else:
        print(odd[idx_odd],end= " ")
        idx_odd += 1

# 10
# 1 2 3 4 5 6 7 7 9 6