from datetime import datetime
from tkinter import *

from tkcalendar import *


def AddMemberPaymentPanel(self):
    self.Frame_AddMemberPayment = Frame(self.Mainmenuroot, bg="white")
    self.Frame_AddMemberPayment.place(x=250, y=60, width=950, height=950)
    Label(self.Frame_AddMemberPayment, text="Payment Details", font=("Goudy old style", 20, "bold", "underline"),
          fg="#000000",
          bg="#FFFFFF").place(
        x=345, y=10)
    Label(self.Frame_AddMemberPayment, text="Choose Payment Date :", font=("Goudy old style", 15, "bold", "underline"),
          fg="#000000",
          bg="#FFFFFF").place(
        x=50, y=50)
    Label(self.Frame_AddMemberPayment, text="From:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=55, y=100)
    self.datefrom = StringVar(self.Frame_AddMemberPayment, value=self.datefrom)
    self.chooseform = Entry(self.Frame_AddMemberPayment, font=("Goudy old style", 12),
                            fg="#343434",
                            bg="#FFFFFF", textvariable=self.datefrom)
    self.chooseform.place(x=120, y=100, width=200)
    now = datetime.now()
    self.calfrom = Calendar(self.Frame_AddMemberPayment, selectmode='day',
                            year=int(now.year), month=int(now.month),
                            day=int(now.day))

    self.calfrom.place(x=55, y=150)
    Button(self.Frame_AddMemberPayment, text="Get Date", command=self.getdatefrom, bd=0, font=("Goudy old style", 10),
           bg="#F25125",
           fg="#F9F1F1").place(x=55, y=350, width=80, height=40)

    Label(self.Frame_AddMemberPayment, text="To:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=500, y=100)
    self.dateto = StringVar(self.Frame_AddMemberPayment, value=self.dateto)
    self.chooseto = Entry(self.Frame_AddMemberPayment, font=("Goudy old style", 12),
                          fg="#343434",
                          bg="#FFFFFF", textvariable=self.dateto)
    self.chooseto.place(x=550, y=100, width=200)
    self.calto = Calendar(self.Frame_AddMemberPayment, selectmode='day',
                          year=int(now.year), month=int(now.month),
                          day=int(now.day))

    self.calto.place(x=500, y=150)
    Button(self.Frame_AddMemberPayment, text="Get Date", command=self.getdateto, bd=0, font=("Goudy old style", 10),
           bg="#F25125",
           fg="#F9F1F1").place(x=500, y=350, width=80, height=40)
    Label(self.Frame_AddMemberPayment, text="Amount:", font=("Goudy old style", 15, "bold", "underline"),
          fg="#000000",
          bg="#FFFFFF").place(
        x=50, y=420)
    Label(self.Frame_AddMemberPayment, text="Amount:", font=("Goudy old style", 12),
          fg="#000000",
          bg="#FFFFFF").place(
        x=50, y=480)
    self.amount = Entry(self.Frame_AddMemberPayment, font=("Goudy old style", 12),
                        fg="#343434",
                        bg="#FFFFFF")
    self.amount.place(x=150, y=480, width=300)
    Button(self.Frame_AddMemberPayment, text="Submit", command=self.getmemberinfo, bd=0, font=("Goudy old style", 15),
           bg="#F25125",
           fg="#F9F1F1").place(x=772, y=500, width=80, height=40)
