n = int(input())
arr = []
for i in range(n):
    string = input()
    idx = 0
    while idx < len(string):
        num = 0
        has = False
        while idx < len(string) and string[idx].isdigit():
            has = True
            num = num * 10 +  int(string[idx])
            idx += 1
        if(has):
            arr.append(num)
        idx += 1
arr.sort()
print(*arr,sep = "\n")

# 3
# A129h
# G07bxjq3
# aaaaaaa4aaaa