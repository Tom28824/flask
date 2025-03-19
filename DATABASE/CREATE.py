import sqlite3
con = sqlite3.connect('mydatabase.db')
cur = con.cursor()
cur.execute("""CREATE TABLE Employees (
                EmpID INTERGER NOT NULL PRIMARY KEY,
                EmpName VARCHAR(20) NOT NULL,
                HireData Date,
                salary CURRENCY
                )""")
con.commit()
con.close()