from datetime import datetime
from tkinter import *


def updategetdatefrommemberabsnt(self):
    self.updatedatefromabsnt = self.updatecalfrom.get_date()
    date_time_obj = datetime.strptime(self.updatedatefromabsnt, '%m/%d/%y')
    date_time_obj = date_time_obj.strftime("%Y/%m/%d")
    self.updatedatefromabsnt = StringVar(self.Frame_UpdatePaymentAbsnt, value=date_time_obj)

    self.updatechooseform = Entry(self.Frame_UpdatePaymentAbsnt, font=("Goudy old style", 12),
                                  fg="#343434",
                                  bg="#FFFFFF", textvariable=self.updatedatefromabsnt)
    self.updatechooseform.place(x=120, y=100, width=200)
