class user:
    def  __init__(self, date, name, contact) :
        self.l_name = name.split()[-1]
        self.f_name = name 
        self.date = date 
        self.contact = contact
    
    def out(self) :
        return self.f_name + ": " +self.contact  + " " + self.date

with open("SOTAY.txt", "r") as file1:
    inp = file1.read().split('\n')
    ls = []
    while(len(inp) > 0):
        x = inp[0]
        inp.pop(0)
        if(x[:4:] == "Ngay"):
            date = x[5::]
        elif(len(inp) > 0):
            contact = inp[0]
            inp.pop(0)
            a = user(date, x, contact)
            ls.append(a) 
    ls = sorted(ls, key = lambda x : (x.l_name, x.f_name))
with open("DIENTHOAI.txt", "w") as file2:
    for i in ls :
        file2.write(i.out() + '\n')
file1.close()
file2.close()
