def peek(st):
    n = st.pop()
    st.append(n)
    return n 
for t in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    st = []
    res = []
    st.append(arr[n - 1])
    res.append(-1)
    for i in range(n - 2, -1, -1):
        while(len(st) > 0 and arr[i] >= peek(st)):
            st.pop()
        if(len(st) == 0):
            res.append(-1)
        else:
            res.append(peek(st))
        st.append(arr[i])
    res.reverse()
    for i in range(n):
        print(res[i], end= " ")
    print()

    
# 3
# 4
# 4 5 2 25
# 3
# 2 2 2
# 4
# 4 4 5 5