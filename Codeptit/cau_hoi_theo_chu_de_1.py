type = []
cnt = 0
n = int(input())
while(n > 0):
    line = input()
    n -= 1
    type.append(line)
    if(len(line) == 0):
        print(type[0] + ": " + str(len(type) - 2))
        type.clear()
print(type[0] + ": " + str(len(type) - 1)) 

# 9
# Home/accommodation
# What kind of housing/accommodation do you live in?
# Who do you live with?
# How long have you lived there?

# Study
# Describe your education
# What is your area of specialization?
# Why did you choose to study that major?