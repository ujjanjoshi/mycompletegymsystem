import sqlite3
from datetime import datetime

from Modules.Controller.Email.getemail import email_alert


def sendmail(self):
    conn = sqlite3.connect('D:\GymSystem\Modules\Model\gymmanage.db')
    c = conn.cursor()
    now = datetime.now()
    datess = now.strftime("%Y/%m/%d")
    c.execute("Select * from memberdetials where DateExpiry='"+datess+"'")
    datas =c.fetchall()
    if(len(datas)!=0):
            c.execute("select* from counter where id='1'")
            datasss = c.fetchall()[0][1]
            if(datasss!=datess):
                for i in range(len(datas)):
                        emails=datas[i][4]
                        email_alert("Renew of Membership", """
Your Membership is expired. Please renew in time.
Thank You!!
    
From:
RiverField Fitness and Gym
                        """, str(emails))
                c.execute("Update counter set Date='"+datess+"' where id='1'")
    conn.commit()
    conn.close()