from datetime import datetime
from tkinter import *


def updategetdatetomember(self):
    self.updatedateto = self.updatecalto.get_date()
    date_time_obj = datetime.strptime(self.updatedateto, '%m/%d/%y')
    date_time_obj = date_time_obj.strftime("%Y/%m/%d")
    self.updatedateto = StringVar(self.Frame_UpdatePayment, value=date_time_obj)
    self.updatechooseto = Entry(self.Frame_UpdatePayment, font=("Goudy old style", 12),
                                fg="#343434",
                                bg="#FFFFFF", textvariable=self.updatedateto)
    self.updatechooseto.place(x=550, y=100, width=200)
