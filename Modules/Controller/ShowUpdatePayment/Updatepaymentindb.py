import sqlite3
from datetime import datetime
from tkinter import messagebox

from Modules.View.ShowPaymentUpdate.paymnettop import PaymentPanel


def updateintodb(self):
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    c.execute("Update memberdetials Set Month='" + str(self.updatemonths.get()) + "',DatePaid='" + str(
        self.updatedatefrom.get()) +
              "',DateExpiry='" + str(self.updatedateto.get()) + "',Amount='" + str(
        self.updateamount.get()) + "',Status='Active' where M_id=" + str(self.ids))
    c.execute("Select * from memberdetials where M_id=" + str(self.ids))
    datas = c.fetchall()
    now = datetime.now()
    datess = now.strftime("%Y/%m/%d")
    c.execute(
        "Insert into paymentdetails(M_Id,Name,Phoneno,Date,Status) values('" + str(datas[0][0]) + "','" + datas[0][
            1] + "','" + datas[0][3] + "','" + datess + "','Paid')")
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucessful", "Payment Updated")
    PaymentPanel(self)
