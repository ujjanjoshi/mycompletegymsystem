from tkinter import *

from Modules.View.Attendence.showattendencemember import showupattendence


def AttendencePanel(self):
    self.Frame_Attendence = Frame(self.Mainmenuroot, bg="white")
    self.Frame_Attendence.place(x=250, y=60, width=950, height=950)
    Frame_Top = Frame(self.Frame_Attendence, bg="#F98C6E")
    Frame_Top.place(x=0, y=0, width=950, height=60)
    Label(Frame_Top, text="Attendence", font=("Goudy old style", 15, "bold"), fg="#FFFFFF",
          bg="#F98C6E").place(
        x=10, y=15)
    Label(Frame_Top, text="Shift", font=("Goudy old style", 12, "bold"), fg="#FFFFFF",
          bg="#F98C6E").place(
        x=780, y=15)
    options = [
        "....",
        "Morning",
        "Evening"
    ]
    self.shiftsss = StringVar()
    self.shiftsss.set("....")
    self.shifts = OptionMenu(Frame_Top, self.shiftsss, *options, command=self.showattendence)
    self.shifts.configure(background="white")
    self.shifts.place(x=820, y=15, width=100)
    showupattendence(self)
