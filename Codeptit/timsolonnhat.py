tests = int(input())
while tests > 0 :
    ans = -1
    string = input()
    string += 'z'
    num = 0
    for i in range(len(string)):
        if i != 0 and string[i].isalpha() and string[i - 1].isdigit():
            ans = max(ans, num)
            num = 0
        elif string[i].isdigit() :
            num = num*10 + int(string[i]) 
    print(max)
    tests-=1

