from tkinter import *

from Modules.View.ShowPaymentUpdate.showpaymentupdatemember import showupdatepayment


def PaymentPanel(self):
    self.Frame_ViewPaymentUpdate = Frame(self.Mainmenuroot, bg="white")
    self.Frame_ViewPaymentUpdate.place(x=250, y=60, width=950, height=950)
    Frame_Top = Frame(self.Frame_ViewPaymentUpdate, bg="#F98C6E")
    Frame_Top.place(x=0, y=0, width=950, height=60)
    Label(Frame_Top, text="Payment Expiry", font=("Goudy old style", 15, "bold"), fg="#FFFFFF",
          bg="#F98C6E").place(
        x=10, y=15)
    showupdatepayment(self)
