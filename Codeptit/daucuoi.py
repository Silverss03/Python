for t in range(int(input())):
    string = input()
    l_string = r_string = ""
    for i in range(0,2):
        l_string += string[i]
    for i in range(len(string) - 2, len(string)):
        r_string += string[i]
    if(l_string == r_string): print("YES")
    else: print("NO")