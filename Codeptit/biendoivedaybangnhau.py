n = int(input())
arr = [int(i) for i in input().split()]
res = 1e9
idx = 0
for i in range(n):
	tmp = 0
	for j in range(n):
		if(i == j): continue
		tmp += abs(arr[i] - arr[j])
	if(tmp < res):
		res = tmp
		idx = i
print("{} {}".format(res, arr[idx]))

# 8
# 13 5 8 7 9 15 26 34