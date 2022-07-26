import sqlite3
from tkinter import messagebox

from Modules.View.ShowMemberdetails.showmembersdetials import MemeberViewDetailsPanel


def GetfullInfo(self):
    if (self.datefrom.get() == "Choose date" or self.dateto.get() == "Choose date" or self.amount.get() == ""):
        messagebox.showerror("Error", "Fill Required Information for Payment Details")
    else:
        messagebox.showinfo("Sucessful", "Record Added")
        conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
        c = conn.cursor()
        c.execute(
            "Insert into memberdetials(Fullname,Address,Mobileno,Email,Age,Gender,Bloodgroup,Emergencycontactperson,Emergencycontactnumber,Exercise,Month,Shift,DatePaid,DateExpiry,Amount,Status,ApprovedBy) Values(" +
            "'" + self.membersfullname + "','" + self.memberadress + "','" + self.membermobileno + "','" +
            self.memberphonene + "','" + self.membeberage + "','" + self.membergender + "','" +
            self.memberbloodgroup + "','" + self.memberemergencycontactperson + "','" + self.memberemergencycontactnumber + "','" +
            self.memberchoosegym_cardio + "','" + self.memberchoosemonths + "','" + self.memberchooseshift + "','" +
            self.datefrom.get() + "','" +
            self.dateto.get() + "','" +
            self.amount.get() + "'," +
            "'Active','" + self.name + "')"
        )
        conn.commit()
        conn.close()
        MemeberViewDetailsPanel(self)
