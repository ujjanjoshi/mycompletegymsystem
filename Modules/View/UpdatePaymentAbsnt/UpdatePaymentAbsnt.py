from datetime import datetime
from tkinter import *
from tkcalendar import *


def UpdatePaymentAfterAbsent(self, num):
    self.idss = num
    self.Frame_UpdatePaymentAbsnt = Frame(self.Mainmenuroot, bg="white")
    self.Frame_UpdatePaymentAbsnt.place(x=250, y=60, width=950, height=950)
    Label(self.Frame_UpdatePaymentAbsnt, text="Payment Details", font=("Goudy old style", 20, "bold", "underline"),
          fg="#000000",
          bg="#FFFFFF").place(
        x=345, y=10)
    Label(self.Frame_UpdatePaymentAbsnt, text="Choose Payment Date :", font=("Goudy old style", 15, "bold", "underline"),
          fg="#000000",
          bg="#FFFFFF").place(
        x=50, y=50)
    Label(self.Frame_UpdatePaymentAbsnt, text="From:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=55, y=100)
    self.updatedatefromabsnt = StringVar(self.Frame_UpdatePaymentAbsnt, value=self.updatedatefromabsnt)
    self.updatechooseform = Entry(self.Frame_UpdatePaymentAbsnt, font=("Goudy old style", 12),
                                  fg="#343434",
                                  bg="#FFFFFF", textvariable=self.updatedatefromabsnt)
    self.updatechooseform.place(x=120, y=100, width=200)
    now = datetime.now()
    self.updatecalfrom = Calendar(self.Frame_UpdatePaymentAbsnt, selectmode='day',
                                  year=int(now.year), month=int(now.month),
                                  day=int(now.day))
    self.updatecalfrom.place(x=55, y=150)
    Button(self.Frame_UpdatePaymentAbsnt, text="Get Date", command=self.updategetdatefromabsnts, bd=0,
           font=("Goudy old style", 10),
           bg="#F25125",
           fg="#F9F1F1").place(x=55, y=350, width=80, height=40)

    Label(self.Frame_UpdatePaymentAbsnt, text="To:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=500, y=100)
    self.updatedatetoabsnt = StringVar(self.Frame_UpdatePaymentAbsnt, value=self.updatedatetoabsnt)
    self.updatechooseto = Entry(self.Frame_UpdatePaymentAbsnt, font=("Goudy old style", 12),
                                fg="#343434",
                                bg="#FFFFFF", textvariable=self.updatedatetoabsnt)
    self.updatechooseto.place(x=550, y=100, width=200)
    self.updatecalto = Calendar(self.Frame_UpdatePaymentAbsnt, selectmode='day',
                                year=int(now.year), month=int(now.month),
                                day=int(now.day))
    self.updatecalto.pack()
    self.updatecalto.place(x=500, y=150)
    Button(self.Frame_UpdatePaymentAbsnt, text="Get Date", command=self.updategetdatetoabsnts, bd=0, font=("Goudy old style", 10),
           bg="#F25125",
           fg="#F9F1F1").place(x=500, y=350, width=80, height=40)
    Button(self.Frame_UpdatePaymentAbsnt, text="Update", command=self.updatedbs, bd=0, font=("Goudy old style", 15),
           bg="#F25125",
           fg="#F9F1F1").place(x=772, y=500, width=80, height=40)
