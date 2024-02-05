def check(input):
    if(input == input[::-1]):
        return  True
    else:
        return  False
with open("VANBAN.in", "r") as file1:
    res = []
    curr = ""
    string = []
    printed = []
    while(True):
        line = file1.read()
        if not line:
            break
        string += line.strip().split()
    for i in string:
        if check(i) and len(res) == 0:
            res.append(line)
            curr = line
        if len(res) != 0 and check(i) and len(i) > len(curr):
            res.clear()
            curr = i
            res.append(i)
        elif len(res) != 0 and check(i) and len(i) == len(curr):
            res.append(i)
    for i in res:
        if i not in printed:
            print(i,end= " ")
            print(res.count(i))
            printed.append(i)
file1.close()