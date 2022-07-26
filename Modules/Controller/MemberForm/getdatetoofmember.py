from datetime import datetime
from tkinter import *


def getdatetomember(self):
    self.dateto = self.calto.get_date()
    date_time_obj = datetime.strptime(self.dateto, '%m/%d/%y')
    date_time_obj = date_time_obj.strftime("%Y/%m/%d")
    self.dateto = StringVar(self.Frame_AddMemberPayment, value=date_time_obj)
    self.chooseto = Entry(self.Frame_AddMemberPayment, font=("Goudy old style", 12),
                          fg="#343434",
                          bg="#FFFFFF", textvariable=self.dateto)
    self.chooseto.place(x=550, y=100, width=200)
