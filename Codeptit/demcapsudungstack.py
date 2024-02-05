n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

stack = []
result = 0

for i in range(n):
    while stack and arr[i] >= arr[stack[-1]]:
        j = stack.pop()
        result += i - j if arr[j] != arr[i] else i - j - 1
    stack.append(i)

print(result)



# 7
# 2
# 4
# 1
# 2
# 2
# 5
# 1

