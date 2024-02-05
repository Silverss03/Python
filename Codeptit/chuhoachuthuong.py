string = input()
upper = lower = 0
for i in range(len(string)):
    if(string[i] >= 'a' and string[i] <= 'z'): lower+=1
    elif(string[i] >= 'A' and string[i] <= 'Z'): upper += 1
if(lower >= upper): print(string.lower())
else: print(string.upper())