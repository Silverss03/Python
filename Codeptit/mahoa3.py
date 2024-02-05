dict = {}
for i in range(26):
    dict[chr(ord('A') + i)] = i
def rotate(string):
    rot = 0
    for i in range(len(string)):
        rot += dict[string[i]]
    res = ""
    for i in range(len(string)):
        res += chr(ord('A') +(dict[string[i]] + rot)%26)
    return res
for t in range(int(input())):
    string = input()
    idx = int(len(string)/2)
    first_half = string[:idx]
    second_half = string[idx:]
    first_half = rotate(first_half)
    second_half = rotate(second_half)
    res = ""
    for i in range(len(second_half)):
        res += chr(ord('A') +(dict[second_half[i]] + dict[first_half[i]])%26)
    print(res)