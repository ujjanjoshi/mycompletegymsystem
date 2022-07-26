import sqlite3
from tkinter import messagebox

from Modules.View.ShowMemberdetails.viewfulldetials import fulldetails


def updateintodbss(self):
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    c.execute("Update memberdetials Set DatePaid='" + str(
            self.updatedatefromabsnt.get()) +
                  "',DateExpiry='" + str(self.updatedatetoabsnt.get()) + "',Status='Active' where M_id=" + str(self.idss))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucessful", "Payment Updated")
    fulldetails(self, self.idss)
