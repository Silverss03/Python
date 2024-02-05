n = int(input())
for i in range(1, n + 1):
    string_a = input()
    letter_a = []
    string_b = input()
    res = True
    for j in range(len(string_a)):
        if(string_a[j] not in letter_a):
            letter_a.append(string_a[j])
    for j in range(len(string_b)):
        if(string_b[j] not in letter_a or string_b.count(string_b[j]) != string_a.count(string_b[j])):
            res = False
            break
    print(f"Test {i}: ", end= "") 
    if(res):
        print("YES")
    else:
        print("NO")

# 4
# testing
# intestg
# abc
# aabbbcccc
# abcabcbcc
# aabbbcccc
# abc
# xyz