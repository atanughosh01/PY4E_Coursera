"""This application will read the mailbox data (mbox.txt) and count the number of email
messages per organization (i.e. domain name of the email address) using a database with
the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)

When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with dfferent files,
make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database
as each record is read in the loop, it might take as long as a few minutes to process all the data.
The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop.
In any database program, there is a balance between the number of operations you execute between commits
and the importance of not losing the results of operations that have not yet been committed."""

# import required packages
import sys
import sqlite3

# connect with the database if already present
# if not present create a new one having name 'orgdb.sqlite'
con = sqlite3.connect("orgdb.sqlite")

# return a cursor for the connection.
cur = con.cursor()

# if a table named 'Counts' already exists, skip to next step
cur.execute("DROP TABLE IF EXISTS Counts")

# Create table with 'org' and 'count' as columns
cur.execute("""CREATE TABLE Counts (org TEXT, count INTEGER)""")

# Enter mbox.txt as filename
file = input("\nEnter File Name : ")

# if no input is given consider 'mbox.txt' as input file
if len(file) < 1:
    print("Considering 'mbox.txt' as the input file")
    file = "mbox.txt"
try:
    fhand = open(file)
except FileNotFoundError as fe:
    print("EXCEPTION CAUGHT : " + str(fe))
    sys.exit()

for line in fhand:
    if not line.startswith("From: "): continue
    words = line.split()
    email = words[1]                            # parse through the text file and extract email id-s
    org = email.split("@")[1]                   # extract organizations (domains) from emails
    cur.execute("SELECT count FROM Counts WHERE org = ? ", (org,))
    row = cur.fetchone()                        # fetch a row data in each iteration
    if row is None:
        # Insert data if nothing present in row
        cur.execute("""INSERT INTO Counts (org, count) VALUES (?, 1)""", (org,))
    else:
        # Update a row if already data present
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (org,))

# Save (commit) the changes
# commit operation moved outside the loop to speed up the execution
con.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = "SELECT org, count from Counts ORDER BY count DESC"

# print the table in decreasing order of count of domains
print("\nCount     Domain")
print("------    ------")
for row in cur.execute(sqlstr):
    print(row[1], "    ", str(row[0]))
    # print(str(row[0]), " ", row[1])

# close the file and terminate the cursor
fhand.close()
cur.close()
