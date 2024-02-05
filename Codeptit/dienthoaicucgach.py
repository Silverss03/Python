for t in range(int(input())):
    string = input().upper()
    num = ""
    for i in range(len(string)):
        if(string[i] == "A" or string[i] == "B" or string[i] == "C"):
            num += "2"
        elif(string[i] == "D" or string[i] == "E" or string[i] == "F"):
            num += "3"
        elif(string[i] == "G" or string[i] == "H" or string[i] == "I"):
            num += "4"
        elif(string[i] == "J" or string[i] == "K" or string[i] == "L"):
            num += "5"
        elif(string[i] == "M" or string[i] == "N" or string[i] == "O"):
            num += "6"
        elif(string[i] == "P" or string[i] == "Q" or string[i] == "R" or string[i] == "S"):
            num += "7"
        elif(string[i] == "T" or string[i] == "U" or string[i] == "V"):
            num += "8"
        else:
            num += "9"
    if(num == num[::-1]):
        print("YES")
    else:
        print("NO")