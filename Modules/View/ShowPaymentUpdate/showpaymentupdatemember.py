import sqlite3
from tkinter import *
from tkinter import ttk

from Modules.View.ShowPaymentUpdate.showpaymentupdatedetails import showupdatepaymentdetails


def showupdatepayment(self):
    self.updatedateto = "Choose date"
    self.updatedatefrom = "Choose date"
    self.Frame_Upss = Frame(self.Frame_ViewPaymentUpdate, bg="#FFFFFF")
    self.Frame_Upss.place(x=0, y=60, width=950, height=950)
    self.Frame_Ups = LabelFrame(self.Frame_Upss, bg="#FFFFFF")
    self.Frame_Ups.place(height=600)
    self.mycanvas = Canvas(self.Frame_Ups, bg="#FFFFFF")
    self.mycanvas.pack(side=LEFT, fill="both", expand=1)
    self.myframe = Frame(self.mycanvas, bg="#FFFFFF")
    self.myframe.place(x=0, y=60, width=950, height=800)
    self.mycanvas.create_window((0, 0), window=self.myframe, anchor="nw")
    self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion=self.mycanvas.bbox('all')))
    yscrollbar = ttk.Scrollbar(self.Frame_Ups, orient="vertical", command=self.mycanvas.yview)
    yscrollbar.pack(fill="y", side=RIGHT)
    self.mycanvas.configure(yscrollcommand=yscrollbar.set)
    self.Frame_Ups.pack(fill="both", padx=1, pady=1)
    Label(self.myframe, text="M_ID", anchor="center", background="#FFFFFF",
          font=("Goudy old style", 12, "bold")).grid(
        row=0, column=1, sticky="ew", ipadx=80)
    Label(self.myframe, text="Name", anchor="center", background="#FFFFFF",
          font=("Goudy old style", 12, "bold")).grid(
        row=0, column=2, sticky="ew", ipadx=80)
    Label(self.myframe, text="PhoneNo", anchor="center", background="#FFFFFF",
          font=("Goudy old style", 12, "bold")).grid(
        row=0, column=3, sticky="ew", ipadx=80)
    Label(self.myframe, text="Status", anchor="center", background="#FFFFFF",
          font=("Goudy old style", 12, "bold")).grid(
        row=0, column=4, sticky="ew", ipadx=50)
    Label(self.myframe, text="Update", anchor="center", background="#FFFFFF",
          font=("Goudy old style", 12, "bold")).grid(row=0, column=5, sticky="ew", ipadx=20)
    Label(self.myframe, text="", anchor="center", background="#FFFFFF",
          font=("Goudy old style", 12, "bold")).grid(row=0, column=6, sticky="ew", ipadx=50)
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    c.execute("Select * from memberdetials where Status='Deactive'")
    self.datambr = c.fetchall()
    self.lengthofdata = len(self.datambr)
    row = 1
    for k in range(self.lengthofdata):
        nr = self.datambr[k][0]
        self.membrid = self.datambr[k][0]
        self.mebmrnm = self.datambr[k][1]
        self.membrphn = self.datambr[k][3]
        self.membrstatus = self.datambr[k][16]
        nr_label = Label(self.myframe, text=self.membrid, anchor="center", background="#FFFFFF",
                         font=("Goudy old style", 12))
        name_label = Label(self.myframe, text=self.mebmrnm, anchor="center", background="#FFFFFF",
                           font=("Goudy old style", 12))
        expiry_label = Label(self.myframe, text=self.membrphn, anchor="center",
                             background="#FFFFFF",
                             font=("Goudy old style", 12))
        remaning_label = Label(self.myframe, text=self.membrstatus, anchor="center",
                               background="#FFFFFF",
                               font=("Goudy old style", 12))
        action_button = Button(self.myframe, text="Update",
                               background="#FFFFFF", command=lambda nr=nr: self.updtepayment(nr))
        action_button.place(width=10)
        nr_label.grid(row=row, column=1, sticky="ew", ipady=10)
        name_label.grid(row=row, column=2, sticky="ew")
        expiry_label.grid(row=row, column=3, sticky="ew")
        remaning_label.grid(row=row, column=4, sticky="ew")
        action_button.grid(row=row, column=5, sticky="ew")
        row = row + 1
    showupdatepaymentdetails(self)
