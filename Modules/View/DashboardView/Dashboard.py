import sqlite3
from datetime import datetime
from tkinter import *
from Modules.Controller.Email.getemail import email_alert


def DashBoardPanel(self):
    Frame_profile = Frame(self.Mainmenuroot, bg="white")
    Frame_profile.place(x=250, y=60, width=950, height=950)
    Label(Frame_profile, text="Dashboard", font=("Goudy old style", 20, "bold"), fg="black",
          bg="#FFFFFF").place(
        x=50, y=20)
    Frame_totalmembers = Frame(Frame_profile, bg="#FFFFFF", highlightbackground="black", highlightthickness=2)
    Frame_totalmembers.place(x=50, y=90, width=250, height=200)
    Label(Frame_totalmembers, text="Total Members", font=("Goudy old style", 20, "bold"), fg="#000000",
         bg="#FFFFFF").place(
        x=35, y=10)
    Frame_line = Frame(Frame_totalmembers, bg="black")
    Frame_line.place(x=0, y=50, width=250, height=5)
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    c.execute("Select * from memberdetials")
    datas=len(c.fetchall())
    Label(Frame_totalmembers, text=str(datas), font=("Goudy old style", 80, "bold"), fg="#000000",
          bg="#FFFFFF").place(
        x=68, y=55)
    Frame_activemembers = Frame(Frame_profile, bg="#FFFFFF", highlightbackground="black", highlightthickness=2)
    Frame_activemembers.place(x=350, y=90, width=250, height=200)
    Label(Frame_activemembers, text="Active Members", font=("Goudy old style", 20, "bold"), fg="#000000",
          bg="#FFFFFF").place(
        x=30, y=10)
    Frame_line = Frame(Frame_activemembers, bg="black")
    Frame_line.place(x=0, y=50, width=250, height=5)
    c.execute("Select * from memberdetials where Status='Active'")
    datas = len(c.fetchall())
    Label(Frame_activemembers, text=str(datas), font=("Goudy old style", 80, "bold"), fg="#000000",
          bg="#FFFFFF").place(
        x=68, y=55)
    Frame_deactivemembers = Frame(Frame_profile, bg="#FFFFFF", highlightbackground="black", highlightthickness=2)
    Frame_deactivemembers.place(x=650, y=90, width=250, height=200)
    Label(Frame_deactivemembers, text="Deactive Members", font=("Goudy old style", 20, "bold"), fg="#000000",
          bg="#FFFFFF").place(
        x=20, y=10)
    Frame_line = Frame(Frame_deactivemembers, bg="black")
    Frame_line.place(x=0, y=50, width=250, height=5)
    c.execute("Select * from memberdetials where Status='Deactive'")
    datas = len(c.fetchall())
    Label(Frame_deactivemembers, text=str(datas), font=("Goudy old style", 80, "bold"), fg="#000000",
                  bg="#FFFFFF").place(
                x=68, y=55)
    Frame_notificaiton = Frame(Frame_profile, bg="#FFFFFF", highlightbackground="black", highlightthickness=2)
    Frame_notificaiton.place(x=50, y=350, width=850, height=200)
    Label(Frame_notificaiton, text="Notification", font=("Goudy old style", 20, "bold"), fg="#000000",
          bg="#FFFFFF").place(
        x=20, y=10)
    Frame_line = Frame(Frame_notificaiton, bg="black")
    Frame_line.place(x=0, y=50, width=850, height=5)
    now = datetime.now()
    datess = now.strftime("%Y/%m/%d")
    c.execute("Select * from memberdetials where DateExpiry='"+datess+"'")
    datas =c.fetchall()
    if(len(datas)!=0):
        for i in range(len(datas)):
            id=datas[i][0]
            name=datas[i][1]
            Label(Frame_notificaiton, text="The member id "+str(id)+" and name "+str(name)+" whose membership has been expired today.", font=("Goudy old style", 15, "bold"), fg="#000000",
                  bg="#FFFFFF").place(
                x=20, y=60)
    else:
        Label(Frame_notificaiton,
              text="No Notification",
              font=("Goudy old style", 15, "bold"), fg="#000000",
              bg="#FFFFFF").place(
            x=20, y=60)
    conn.commit()
    conn.close()
