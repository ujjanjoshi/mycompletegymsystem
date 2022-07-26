import sqlite3
from tkinter import messagebox

from Modules.View.ShowMemberdetails.showmembertable import showmemberstable


def showmemberdetails(self):
    pass


def memberdelete(self, num):
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    c.execute("Delete from memberdetials where M_id=" + str(num))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucessful", "Record Deleted")
    showmemberstable(self)
