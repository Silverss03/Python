lines = []
while True:
    res = "" 
    try:
        line = input().strip()
        if(line[-1] != "." and line[-1] != "?" and line[-1] != "!"):
            line += "."
        arr = line.split()
        arr[0] = arr[0].capitalize()
        res += arr[0] + " "
        for i in range(1, len(arr)):
            if(i < len(arr) - 1 and (arr[i + 1] == "!" or arr[i + 1] == "." or arr[i + 1] == "?")):
                res += arr[i].lower()
            else:
                res += arr[i].lower() + " "
        lines.append(res)
    except EOFError:
        break
for i in range(len(lines)):
    print(lines[i])
    