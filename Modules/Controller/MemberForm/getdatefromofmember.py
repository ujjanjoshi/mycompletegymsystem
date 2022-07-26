from datetime import datetime
from tkinter import *


def getdatefrommember(self):
    self.datefrom = self.calfrom.get_date()
    date_time_obj = datetime.strptime(self.datefrom, '%m/%d/%y')
    date_time_obj = date_time_obj.strftime("%Y/%m/%d")
    self.datefrom = StringVar(self.Frame_AddMemberPayment, value=date_time_obj)
    self.chooseform = Entry(self.Frame_AddMemberPayment, font=("Goudy old style", 12),
                            fg="#343434",
                            bg="#FFFFFF", textvariable=self.datefrom)
    self.chooseform.place(x=120, y=100, width=200)
