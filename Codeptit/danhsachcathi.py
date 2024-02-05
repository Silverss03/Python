class cathi:
    def  __init__(self, ID_n, date, time, room) :
        (self.ID) = 'C' + str(ID_n).zfill(3)
        self.date = date
        self.time = time
        self.room = room
        (self.year) = int(self.date[-4:])
        (self.month) = int(self.date[3:5])
        (self.day) = int(self.date[:2])
        (self.hour) = int(self.time[:2])
        (self.minute) = int(self.time[-2:])
    def out(self):
        print((self.ID) + " " + self.date + " " + self.time + " " + self.room)
    def __lt__(self, obj):
        if((self.year) == (obj.year)):
            if((self.month) == (obj.month)):
                if((self.day) == (obj.day)):
                    if((self.hour) == (obj.hour)):
                        if((self.minute) == (obj.minute)):
                            return (self.ID) < (obj.ID)
                        else:
                            return (self.minute) < (obj.minute) 
                    else:
                        return (self.hour) < (obj.hour)
                else:
                    return (self.day) < (obj.day)
            else:
                return (self.month) < (obj.month)
        else:
            return (self.year) < (obj.year)
    def __gt__(self, obj):
        if((self.year) == (obj.year)):
            if((self.month) == (obj.month)):
                if((self.day) == (obj.day)):
                    if((self.hour) == (obj.hour)):
                        if((self.minute) == (obj.minute)):
                            return (self.ID) > (obj.ID)
                        else:
                            return (self.minute) > (obj.minute) 
                    else:
                        return (self.hour) > (obj.hour)
                else:
                    return (self.day) > (obj.day)
            else:
                return (self.month) > (obj.month)
        else:
            return (self.year) > (obj.year)
        
    def __le__(self, obj):
        if((self.year) == (obj.year)):
            if((self.month) == (obj.month)):
                if((self.day) == (obj.day)):
                    if((self.hour) == (obj.hour)):
                        if((self.minute) == (obj.minute)):
                            return (self.ID) <= (obj.ID)
                        else:
                            return (self.minute) <= (obj.minute) 
                    else:
                        return (self.hour) <= (obj.hour)
                else:
                    return (self.day) <= (obj.day)
            else:
                return (self.month) <= (obj.month)
        else:
            return (self.year) <= (obj.year)

    def __ge__(self, obj):
        if((self.year) == (obj.year)):
            if((self.month) == (obj.month)):
                if((self.day) == (obj.day)):
                    if((self.hour) == (obj.hour)):
                        if((self.minute) == (obj.minute)):
                            return (self.ID) >= (obj.ID)
                        else:
                            return (self.minute) >= (obj.minute) 
                    else:
                        return (self.hour) >= (obj.hour)
                else:
                    return (self.day) >= (obj.day)
            else:
                return (self.month) >= (obj.month)
        else:
            return (self.year) >= (obj.year)  
    
    
with open("CATHI.in", "r") as file1:
    num = int(file1.readline())
    res = list()
    for t in range(1, num + 1):
        day = file1.readline().replace("\n", "")
        time = file1.readline().replace("\n", "")
        room = file1.readline().replace("\n", "")
        a = cathi(t, day, time, room)
        res.append(a)
    res = sorted(res)
    for i in res:
        i.out()
    
file1.close()