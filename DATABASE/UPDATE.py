import sqlite3
con = sqlite3.connect('mydatabase.db')
cur = con.cursor()
cur.execute(""" UPDATE Employees
                SET Salary = Salary * 1.1
                WHERE EmpID = 1122
            """)
con.commit()
con.close()
