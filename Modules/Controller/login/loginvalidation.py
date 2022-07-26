import sqlite3

def LoginValidation(username, password):
    usr = username.upper()
    flag = 1
    password = password.lower()
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    c.execute("Select * from login where Username='" + usr + "' and Password='" + password + "'")
    lenoflogin = len(c.fetchall())
    if (lenoflogin == 1):
        return flag
    conn.commit()
    conn.close()
