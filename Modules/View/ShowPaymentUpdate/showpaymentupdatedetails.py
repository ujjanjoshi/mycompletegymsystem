import sqlite3
from datetime import datetime
from tkinter import *
from tkinter import ttk


def showupdatepaymentdetails(self):
    self.Frame_Down = LabelFrame(self.Frame_Upss, bg="#FFFFFF")
    self.Frame_Down.place(x=100, height=00)
    self.mycanvass = Canvas(self.Frame_Down, bg="#FFFFFF")
    self.mycanvass.pack(side=LEFT, fill="both", expand=1)
    self.myframes = Frame(self.mycanvass, bg="#FFFFFF")
    self.myframes.place(x=0, y=60, width=950, height=800)
    self.mycanvass.create_window((0, 0), window=self.myframes, anchor="nw")
    self.mycanvass.bind('<Configure>', lambda e: self.mycanvass.configure(scrollregion=self.mycanvass.bbox('all')))
    yscrollbar = ttk.Scrollbar(self.Frame_Down, orient="vertical", command=self.mycanvass.yview)
    yscrollbar.pack(fill="y", side=RIGHT)
    self.mycanvass.configure(yscrollcommand=yscrollbar.set)
    self.Frame_Down.pack(fill="both", padx=1, pady=1)
    Label(self.myframes, text="M_ID", anchor="center", background="#FFFFFF",
          font=("Goudy old style", 12, "bold")).grid(
        row=0, column=1, sticky="ew", ipadx=90)
    Label(self.myframes, text="Name", anchor="center", background="#FFFFFF",
          font=("Goudy old style", 12, "bold")).grid(
        row=0, column=2, sticky="ew", ipadx=90)
    Label(self.myframes, text="PhoneNo", anchor="center", background="#FFFFFF",
          font=("Goudy old style", 12, "bold")).grid(
        row=0, column=3, sticky="ew", ipadx=90)
    Label(self.myframes, text="Status", anchor="center", background="#FFFFFF",
          font=("Goudy old style", 12, "bold")).grid(
        row=0, column=4, sticky="ew", ipadx=90)
    Label(self.myframes, text="", anchor="center", background="#FFFFFF",
          font=("Goudy old style", 12, "bold")).grid(row=0, column=6, sticky="ew", ipadx=50)
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    now = datetime.now()
    datess = now.strftime("%Y/%m/%d")
    c.execute("Select * from paymentdetails where Date='" + str(datess) + "'")
    self.datambr = c.fetchall()
    self.lengthofdata = len(self.datambr)
    row = 1
    for k in range(self.lengthofdata):
        nr = self.datambr[k][0]
        self.mid = self.datambr[k][0]
        self.mnm = self.datambr[k][1]
        self.moh = self.datambr[k][2]
        self.paymentstatus = self.datambr[k][4]
        nr_label = Label(self.myframes, text=self.mid, anchor="center", background="#FFFFFF",
                         font=("Goudy old style", 12))
        name_label = Label(self.myframes, text=self.mnm, anchor="center", background="#FFFFFF",
                           font=("Goudy old style", 12))
        expiry_label = Label(self.myframes, text=self.moh, anchor="center",
                             background="#FFFFFF",
                             font=("Goudy old style", 12))
        remaning_label = Label(self.myframes, text=self.paymentstatus, anchor="center",
                               background="#FFFFFF",
                               font=("Goudy old style", 12))
        nr_label.grid(row=row, column=1, sticky="ew", ipady=10)
        name_label.grid(row=row, column=2, sticky="ew")
        expiry_label.grid(row=row, column=3, sticky="ew")
        remaning_label.grid(row=row, column=4, sticky="ew")
        row = row + 1
