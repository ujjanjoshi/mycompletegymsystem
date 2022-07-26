import sqlite3

# conn=sqlite3.connect('gymmanage.db')
# c=conn.cursor()
# c.execute("""
# Select * from logindetails where Username="Rv001"
# """)
# print(c.fetchall()[0][1])
# conn.commit()
# conn.close()
conn = sqlite3.connect('gymmanage.db')
c = conn.cursor()
c.execute("""
Create table attendencedetails(
        M_id int,
        Name text,
        Phonene text,
        Status text
        )
""")
# print(c.fetchall()[0][1])
conn.commit()
conn.close()
