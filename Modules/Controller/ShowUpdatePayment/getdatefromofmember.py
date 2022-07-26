from datetime import datetime
from tkinter import *


def updategetdatefrommember(self):
    self.updatedatefrom = self.updatecalfrom.get_date()
    date_time_obj = datetime.strptime(self.updatedatefrom, '%m/%d/%y')
    date_time_obj = date_time_obj.strftime("%Y/%m/%d")
    self.updatedatefrom = StringVar(self.Frame_UpdatePayment, value=date_time_obj)

    self.updatechooseform = Entry(self.Frame_UpdatePayment, font=("Goudy old style", 12),
                                  fg="#343434",
                                  bg="#FFFFFF", textvariable=self.updatedatefrom)
    self.updatechooseform.place(x=120, y=100, width=200)
