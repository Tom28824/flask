import sqlite3
con = sqlite3.connect('mydatabase.db')
cur = con.cursor()
cur.execute(""" INSERT INTO Employees (EmpID, EmpName, HireData, Salary)
                VALUES (1122, 'Bloggs', '#1/1/2000#', 18000)
            """)
con.commit()
con.close()
