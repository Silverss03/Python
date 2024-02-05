n = input()
arr = [float(i) for i in input().split()]
a = max(arr)
b = min(arr)
n = 0 
sum = 0 
for i in arr :
    if(i == a) or (i == b):
        continue
    else:
        sum += i
        n += 1
print("{:.2f}".format(sum/n))