from datetime import datetime
from tkinter import *


def updategetdatetomemberabsnt(self):
    self.updatedatetoabsnt = self.updatecalto.get_date()
    date_time_obj = datetime.strptime(self.updatedatetoabsnt, '%m/%d/%y')
    date_time_obj = date_time_obj.strftime("%Y/%m/%d")
    self.updatedatetoabsnt = StringVar(self.Frame_UpdatePaymentAbsnt, value=date_time_obj)
    self.updatechooseto = Entry(self.Frame_UpdatePaymentAbsnt, font=("Goudy old style", 12),
                                fg="#343434",
                                bg="#FFFFFF", textvariable=self.updatedatetoabsnt)
    self.updatechooseto.place(x=550, y=100, width=200)
