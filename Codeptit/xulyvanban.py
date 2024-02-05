import re
res = "" 
while True:
    try:
        line = input()
        res += line
        if not line:
            break
    except EOFError:
        break
sens = re.findall("[\w\s,:]+", res)
for i in sens:
    tmp = i.lower().split()
    tmp[0] = tmp[0].title()
    print(" ".join(tmp))