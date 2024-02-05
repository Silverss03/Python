string = input()
num = string.split(" ")
a, b = int(num[0]), int(num[1])
if(a == 0 and b != 0):
    print("VN")
elif(a == 0 and b == 0):
    print("VSN")
else:
    res = float(-b/a)
    print(f"{res:.2f}")