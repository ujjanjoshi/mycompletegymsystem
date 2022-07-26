import sqlite3
from datetime import datetime
from tkinter import messagebox

from Modules.View.Attendence.attendence import AttendencePanel


def presentmembers(self, num):
    self.ids = num
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    c.execute("Select * from memberdetials where M_id=" + str(self.ids))
    datas = c.fetchall()
    now = datetime.now()
    datess = now.strftime("%Y/%m/%d")
    c.execute(
        "Insert into attendencedetails(M_Id,Name,Phoneno,Date,Status) values('" + str(datas[0][0]) + "','" + datas[0][
            1] + "','" + datas[0][3] + "','" + datess + "','Present')")
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucessful", "Attendence")
    AttendencePanel(self)
