import sqlite3
from tkinter import *



def memberdetaialsdisplay(self, num):
    nr=num
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    c.execute("Select * from memberdetials where M_id=" + str(num))
    datambr = c.fetchall()
    Label(self.Frame_Memberprofile, text=datambr[0][0], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=300, y=80)
    Label(self.Frame_Memberprofile, text=datambr[0][1], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=300, y=130)
    Label(self.Frame_Memberprofile, text=datambr[0][7], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=720, y=130)
    Label(self.Frame_Memberprofile, text=datambr[0][2], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=300, y=180)
    Label(self.Frame_Memberprofile, text=datambr[0][5], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=720, y=180)
    Label(self.Frame_Memberprofile, text=datambr[0][4], font=("Goudy old style", 13, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=250, y=230)
    Label(self.Frame_Memberprofile, text=datambr[0][3], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=720, y=230)
    Label(self.Frame_Memberprofile, text=datambr[0][10], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=300, y=280)
    Label(self.Frame_Memberprofile, text=datambr[0][6], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=720, y=280)
    Label(self.Frame_Memberprofile, text=datambr[0][13], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=300, y=330)
    Label(self.Frame_Memberprofile, text=datambr[0][14], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=720, y=330)
    Label(self.Frame_Memberprofile, text=datambr[0][11], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=300, y=380)
    Label(self.Frame_Memberprofile, text=datambr[0][15], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=720, y=380)
    Label(self.Frame_Memberprofile, text=datambr[0][16], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=300, y=430)
    Label(self.Frame_Memberprofile, text=datambr[0][17], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=720, y=430)
    Label(self.Frame_Memberprofile, text=datambr[0][12], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=300, y=480)
    conn.commit()
    conn.close()
    Label(self.Frame_Memberprofile, text=datambr[0][12], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=300, y=480)
    Button(self.Frame_Memberprofile, text="Edit Payment", command=lambda nr=nr: self.updateaftrasbnt(nr), bd=0,
           font=("Goudy old style", 15),
           bg="#F25125",
           fg="#F9F1F1").place(x=730, y=500, width=150, height=40)
