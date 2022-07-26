import sqlite3


def infofetch(username):
    usr = username.upper()
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    c.execute("Select * from logindetails where Username='" + usr + "'")
    infodetails = c.fetchall()
    lst = [str(infodetails[0][0]), infodetails[0][1], infodetails[0][2], infodetails[0][3], infodetails[0][4],
           infodetails[0][5]]
    return lst
    conn.commit()
    conn.close()
