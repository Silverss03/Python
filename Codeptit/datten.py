res = []
def act(i, arr, n, k, string):
	global res
	for j in range(arr[i - 1] + 1, n + 1):
		arr[i] = j
		if(i == k ):
			s = ""
			for m in range(1,k + 1):
				s += string[arr[m] - 1] + " "
			res.append(s)
		else:
			act(i + 1, arr, n, k, string)
				
n, k = [int(i) for i in input().split()]
string = input().split()
ls = []
for i in string :
	if i not in ls :
		ls.append(i) 
n = len(ls)
ls.sort()
arr = [0] * n
act(1, arr,n,k, ls)
res.sort()
print(*res, sep= "\n")

# 6 2
# DONG TAY NAM BAC TAY BAC