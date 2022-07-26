import sqlite3
from datetime import datetime


def deactivatemember(self):
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    c.execute("Select * from memberdetials")
    datas = c.fetchall()
    now = datetime.now()
    datess = now.strftime("%Y/%m/%d")
    for i in range(len(datas)):
        if (datas[i][14] != None):
            if (datas[i][14] == str(datess)):
                c.execute("Update memberdetials set Status='Deactive' where M_id='" + str(datas[i][0]) + "'")

    conn.commit()
    conn.close()
