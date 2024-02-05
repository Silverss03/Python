with open("CONTACT.in", "r") as file1:
    res = list()
    while(True):
        line = file1.readline()
        if not line:
            break
        email = line.strip().lower()
        if(email not in res and email != ""):
            res.append(email)
    res = sorted(res)
    for i in res:
        print(i)
file1.close()