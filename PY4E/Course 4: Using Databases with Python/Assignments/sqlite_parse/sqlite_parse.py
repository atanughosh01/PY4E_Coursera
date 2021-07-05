"""Program to test sqlite DB parsing"""

import sqlite3

con = sqlite3.connect("emaildb.sqlite")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

# Create table
cur.execute("""CREATE TABLE Counts (email TEXT, count INTEGER)""")

# Enter mbox-short.txt as filename
file = input("Enter File Name : ")
if len(file) < 1: file = "mbox-short.txt"
fhand = open(file)

for line in fhand:
    if not line.startswith("From: "): continue
    words = line.split()
    email = words[1]
    cur.execute("SELECT count FROM Counts WHERE email = ? ", (email,))
    row = cur.fetchone()
    if row is None:
        # Insert a row of data
        cur.execute("""INSERT INTO Counts (email, count) VALUES (?, 1)""", (email,))
    else:
        # Update a row of data
        cur.execute("UPDATE Counts SET count = count + 1 WHERE email = ?", (email,))
    # Save (commit) the changes
    con.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = "SELECT email, count from Counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(str(row[0]), " ", row[1])

fhand.close()
cur.close()
