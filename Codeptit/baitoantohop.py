n, k = [int(i) for i in input().split()]
arr = list(set([int(i) for i in input().split()]))
n = len(arr)
comb = [0] * (k + 1)
def act(i):
    for j in range (comb[i - 1] + 1, n + 1):
        comb[i] = j 
        if(i == k):
            for h in range(1, k + 1):
                print(arr[comb[h] - 1], end = " ")
            print()
        else:
            act(i + 1)
act(1)