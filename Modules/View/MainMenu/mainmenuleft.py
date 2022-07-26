from tkinter import *


def leftPanel(self):
    self.Frame_left = Frame(self.Mainmenuroot, bg="#343434")
    self.Frame_left.place(x=0, y=0, width=250, height=int(self.height))
    self.time()
    Button(self.Frame_left, text="Dashboard", command=self.dashboard, bd=0, font=("Goudy old style", 18),
           fg="white",
           bg="#343434").place(x=35, y=300)
    Button(self.Frame_left, text="Add Members", command=self.addmembers, bd=0, font=("Goudy old style", 18),
           fg="white",
           bg="#343434").place(x=35, y=350)
    Button(self.Frame_left, text="Member Details", command=self.showmemberdetails, bd=0, font=("Goudy old style", 18),
           fg="white",
           bg="#343434").place(x=35, y=400)
    Button(self.Frame_left, text="Payment", bd=0, command=self.paymentdetials, font=("Goudy old style", 18),
           fg="white",
           bg="#343434").place(x=35, y=450)
    Button(self.Frame_left, text="Attendance", command=self.attendnce, bd=0, font=("Goudy old style", 18),
           fg="white",
           bg="#343434").place(x=35, y=500)
    Button(self.Frame_left, text="Log Out", command=self.logout, bd=0, font=("Goudy old style", 15),
           bg="white",
           fg="red").place(x=40, y=580, width=150, height=40)
