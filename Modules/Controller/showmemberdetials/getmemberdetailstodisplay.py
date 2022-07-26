import sqlite3
from tkinter import *


def showmemberinfo(self, row, month, shift):
    self.membrid = ""
    self.mebmrnm = ""
    self.membrphn = ""
    self.membrstatus = ""
    self.datambr = ""
    self.recntnum = 0
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    c.execute("Select * from memberdetials")
    self.datambr = c.fetchall()
    self.recntnum = len(self.datambr)
    if (month == "1month" and shift == "...."):
        c.execute("Select * from memberdetials where Month='1month'")
        self.datambr = c.fetchall()
        self.lengthofdata = len(self.datambr)
        self.ro = 0
    if (month == "3months" and shift == "...."):
        c.execute("Select * from memberdetials where Month='3months'")
        self.datambr = c.fetchall()
        self.lengthofdata = len(self.datambr)
        self.ro = 0
    if (month == "6months" and shift == "...."):
        c.execute("Select * from memberdetials where Month='6months'")
        self.datambr = c.fetchall()
        self.lengthofdata = len(self.datambr)
        self.ro = 0
    if (month == "...." and shift == "Morning"):
        c.execute("Select * from memberdetials where Shift='Morning'")
        self.datambr = c.fetchall()
        self.lengthofdata = len(self.datambr)
        self.ro = 0
    if (month == "...." and shift == "Evening"):
        c.execute("Select * from memberdetials where Shift='Evening'")
        self.datambr = c.fetchall()
        self.lengthofdata = len(self.datambr)
        self.ro = 0
    if (month == "1month" and shift == "Morning"):
        c.execute("Select * from memberdetials where Month='1month' and Shift='Morning'")
        self.datambr = c.fetchall()
        self.lengthofdata = len(self.datambr)
        self.ro = 0
    if (month == "1month" and shift == "Evening"):
        c.execute("Select * from memberdetials where Month='1month' and Shift='Evening'")
        self.datambr = c.fetchall()
        self.lengthofdata = len(self.datambr)
        self.ro = 0
    if (month == "3months" and shift == "Morning"):
        c.execute("Select * from memberdetials where Month='3months' and Shift='Morning'")
        self.datambr = c.fetchall()
        self.lengthofdata = len(self.datambr)
        self.ro = 0
    if (month == "3months" and shift == "Evening"):
        c.execute("Select * from memberdetials where Month='3months' and Shift='Evening'")
        self.datambr = c.fetchall()
        self.lengthofdata = len(self.datambr)
        self.ro = 0
    if (month == "6months" and shift == "Morning"):
        c.execute("Select * from memberdetials where Month='6months' and Shift='Morning'")
        self.datambr = c.fetchall()
        self.lengthofdata = len(self.datambr)
        self.ro = 0
    if (month == "6months" and shift == "Evening"):
        c.execute("Select * from memberdetials where Month='6months' and Shift='Evening'")
        self.datambr = c.fetchall()
        self.lengthofdata = len(self.datambr)
        self.ro = 0
    if (month == "...." and shift == "...."):
        c.execute("Select * from memberdetials")
        self.datambr = c.fetchall()
        self.lengthofdata = len(self.datambr)
        self.ro = 0
    for k in range(self.recntnum):
        if (k < (self.lengthofdata)):

            self.membrid = self.datambr[k][0]
            nr = self.membrid
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
            action_button = Button(self.myframe, text="View", command=lambda nr=nr: self.fulldetailss(nr),
                                   background="#FFFFFF")
            action_button.place(width=10)
            action_button1 = Button(self.myframe, text="Delete", command=lambda nr=nr: self.delete(nr),
                                    background="#FFFFFF")
            action_button.place(width=10)
            nr_label.grid(row=row, column=1, sticky="ew", ipady=10)
            name_label.grid(row=row, column=2, sticky="ew")
            expiry_label.grid(row=row, column=3, sticky="ew")
            remaning_label.grid(row=row, column=4, sticky="ew")
            action_button.grid(row=row, column=5, sticky="ew")
            action_button1.grid(row=row, column=6, sticky="ew")
            row = row + 1
        else:
            nr_label = Label(self.myframe, text="", anchor="center", background="#FFFFFF",
                             font=("Goudy old style", 12))
            name_label = Label(self.myframe, text="", anchor="center", background="#FFFFFF",
                               font=("Goudy old style", 12))
            expiry_label = Label(self.myframe, text="", anchor="center",
                                 background="#FFFFFF",
                                 font=("Goudy old style", 12))
            remaning_label = Label(self.myframe, text='', anchor="center",
                                   background="#FFFFFF",
                                   font=("Goudy old style", 12))
            action_button = Label(self.myframe, text='', anchor="center",
                                  background="#FFFFFF",
                                  font=("Goudy old style", 12))
            action_button1 = Label(self.myframe, text='', anchor="center",
                                   background="#FFFFFF",
                                   font=("Goudy old style", 12))
            nr_label.grid(row=row, column=1, sticky="ew", ipady=10)
            name_label.grid(row=row, column=2, sticky="ew")
            expiry_label.grid(row=row, column=3, sticky="ew")
            remaning_label.grid(row=row, column=4, sticky="ew")
            action_button.grid(row=row, column=5, sticky="ew")
            action_button1.grid(row=row, column=6, sticky="ew")
            row = row + 1
    conn.commit()
    conn.close()
