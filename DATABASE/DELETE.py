import sqlite3
con = sqlite3.connect('mydatabase.db')
cur = con.cursor()
cur.execute(""" DELETE FROM Employees
                WHERE EmpID = 1122
            """)
con.commit()
con.close()
