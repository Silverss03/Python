def find_max():
    max = -1e8
    res = 0
    for i in range(len(arr_A)):
        if (arr_A[i] + arr_B[i]) > max:
            max = arr_A[i] + arr_B[i] 
            res = i
    return res
n, k = [int(i) for i in input().split()]
arr_A = [int(i) for i in input().split()]
arr_B = [int(i) for i in input().split()]
idx_A = idx_B = find_max()
A_choosen = arr_A[idx_A]
B_choosen = arr_B[idx_B]
while(k > 0):
    if A_choosen < B_choosen:
        arr_A[idx_A] += 1
        A_choosen += 1
        k -= 1
    elif A_choosen > B_choosen:
        arr_B[idx_B] += 1
        B_choosen += 1
        k -= 1
    else:
        if(sum(arr_A) > sum(arr_B)):
            arr_A[idx_A] += 1
            A_choosen += 1
            k -= 1
        else:
            arr_B[idx_B] += 1
            B_choosen += 1
            k -= 1
res = 0 
for i in range(n):
    res += arr_A[i] * arr_B[i]
print(res)

# 6 7
# 2 1 2 3 3 6
# 8 3 3 4 8 8
