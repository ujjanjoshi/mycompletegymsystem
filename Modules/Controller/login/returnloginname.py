import sqlite3


def ReturnName(username):
    usr = username.upper()
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    c.execute("Select Name from logindetails where Username='" + usr + "'")
    name = c.fetchall()[0][0]
    return name
    conn.commit()
    conn.close()
