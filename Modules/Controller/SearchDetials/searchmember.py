def SearchMember(self,event):
    if (event.keysym == "space" or event.keysym == "Shift_L"):
        self.count=self.count
        self.lst.append(event.keysym)
    elif (event.keysym == "BackSpace"):
        if(self.count==-1):
            self.count =-1
        elif(self.count==0):
            self.lst.pop(self.count)
            self.count =-1
        else:
            self.lst.pop(self.count)
            self.count=self.count-1
    else:
        self.count=self.count + 1
        self.lst.append(event.keysym)
