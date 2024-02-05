string = input()
n = len(string)
arr = [0] * n
check = [True] * n
def act(i):
    for j in range(n) :
        if(check[j]):
            arr[i] = j 
            check[j] = False
            if(i == n - 1):
                for k in range(n):
                    print(string[arr[k]], end = "") 
                print()
            act(i + 1)
            check[j] = True
act(0)