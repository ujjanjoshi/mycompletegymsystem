from datetime import datetime
from tkinter import *
from tkcalendar import *


def UpdatePayments(self, num):
    self.ids = num
    self.Frame_UpdatePayment = Frame(self.Mainmenuroot, bg="white")
    self.Frame_UpdatePayment.place(x=250, y=60, width=950, height=950)
    Label(self.Frame_UpdatePayment, text="Payment Details", font=("Goudy old style", 20, "bold", "underline"),
          fg="#000000",
          bg="#FFFFFF").place(
        x=345, y=10)
    Label(self.Frame_UpdatePayment, text="Choose Payment Date :", font=("Goudy old style", 15, "bold", "underline"),
          fg="#000000",
          bg="#FFFFFF").place(
        x=50, y=50)
    Label(self.Frame_UpdatePayment, text="From:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=55, y=100)
    self.updatedatefrom = StringVar(self.Frame_UpdatePayment, value=self.updatedatefrom)
    self.updatechooseform = Entry(self.Frame_UpdatePayment, font=("Goudy old style", 12),
                                  fg="#343434",
                                  bg="#FFFFFF", textvariable=self.updatedatefrom)
    self.updatechooseform.place(x=120, y=100, width=200)
    now = datetime.now()
    self.updatecalfrom = Calendar(self.Frame_UpdatePayment, selectmode='day',
                                  year=int(now.year), month=int(now.month),
                                  day=int(now.day))
    self.updatecalfrom.place(x=55, y=150)
    Button(self.Frame_UpdatePayment, text="Get Date", command=self.updategetdatefrom, bd=0,
           font=("Goudy old style", 10),
           bg="#F25125",
           fg="#F9F1F1").place(x=55, y=350, width=80, height=40)

    Label(self.Frame_UpdatePayment, text="To:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=500, y=100)
    self.updatedateto = StringVar(self.Frame_UpdatePayment, value=self.updatedateto)
    self.updatechooseto = Entry(self.Frame_UpdatePayment, font=("Goudy old style", 12),
                                fg="#343434",
                                bg="#FFFFFF", textvariable=self.updatedateto)
    self.updatechooseto.place(x=550, y=100, width=200)
    self.updatecalto = Calendar(self.Frame_UpdatePayment, selectmode='day',
                                year=int(now.year), month=int(now.month),
                                day=int(now.day))
    self.updatecalto.pack()
    self.updatecalto.place(x=500, y=150)
    Button(self.Frame_UpdatePayment, text="Get Date", command=self.updategetdateto, bd=0, font=("Goudy old style", 10),
           bg="#F25125",
           fg="#F9F1F1").place(x=500, y=350, width=80, height=40)
    Label(self.Frame_UpdatePayment, text="Amount:", font=("Goudy old style", 15, "bold", "underline"),
          fg="#000000",
          bg="#FFFFFF").place(
        x=50, y=420)
    Label(self.Frame_UpdatePayment, text="Amount:", font=("Goudy old style", 12),
          fg="#000000",
          bg="#FFFFFF").place(
        x=50, y=480)
    self.updateamount = Entry(self.Frame_UpdatePayment, font=("Goudy old style", 12),
                              fg="#343434",
                              bg="#FFFFFF")
    self.updateamount.place(x=150, y=480, width=300)
    Label(self.Frame_UpdatePayment, text="Choose Month:", font=("Goudy old style", 15, "bold", "underline"),
          fg="#000000",
          bg="#FFFFFF").place(
        x=500, y=420)
    options = [
        "....",
        "1month",
        "3months",
        "6months"
    ]
    self.updatemonths = StringVar()
    self.updatemonths.set("....")
    self.setmonths = OptionMenu(self.Frame_UpdatePayment, self.updatemonths, *options)
    self.setmonths.configure(background="white")
    self.setmonths.place(x=500, y=475, width=100)
    Button(self.Frame_UpdatePayment, text="Update", command=self.updatedb, bd=0, font=("Goudy old style", 15),
           bg="#F25125",
           fg="#F9F1F1").place(x=772, y=500, width=80, height=40)
