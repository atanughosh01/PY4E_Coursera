"""
** INSTRUCTIONS **
This application will read roster data in JSON format, parse the file, and then produce an SQLite
database that contains a User, Course, and Member table and populate the tables from the data file.

You can base your solution on this code: http://www.py4e.com/code3/roster/roster.py -this code is incomplete
as you need to modify the program to store the role column in the Member table to complete the assignment.

Each student gets their own file for the assignment. Download this file and save it as roster_data.json.
Move the downloaded file into the same folder as your roster.py program.

Once you have made the necessary changes to the program and it has been run successfully
reading the above JSON data, run the following SQL command:

    SELECT User.name, Course.title, Member.role
    FROM User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

The output should look as follows:

    Zohra|si106|0
    Zinedine|si430|0

Once that query gives the correct data, run this query:

    SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X
    FROM User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;

You should get one row with a string that looks like XYZZY53656C696E613333.
(In my case the answer is : XYZZY416164616D736933333430)
"""

# import required packages
import sys
import json
import sqlite3

# connect with the database if already present
# if not present create a new one having name 'rosterdb.sqlite'
con = sqlite3.connect('rosterdb.sqlite')

# return a cursor for the connection.
cur = con.cursor()

# Make some fresh tables using executescript()
cur.executescript("""
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
""")

file_name = input("\nEnter File Name : ")
if len(file_name) < 1:
    print("(Considering 'roster_data.json' as the working file)\n")
    file_name = "roster_data.json"

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

try:
    fhand = open(file_name)
except FileNotFoundError as fe:
    print("EXCEPTION CAUGHT : " + str(fe))
    sys.exit()

str_data = fhand.read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role_id = entry[2]

    print((name, title, role_id))

    cur.execute("""INSERT OR IGNORE INTO User (name) VALUES ( ? )""", (name,))
    cur.execute("SELECT id FROM User WHERE name = ? ", (name,))
    user_id = cur.fetchone()[0]

    cur.execute("""INSERT OR IGNORE INTO Course (title)  VALUES ( ? )""", (title,))
    cur.execute("SELECT id FROM Course WHERE title = ? ", (title,))
    course_id = cur.fetchone()[0]

    cur.execute("""INSERT OR REPLACE INTO Member
           (user_id, course_id, role) VALUES ( ?, ?, ? )""",
                (user_id, course_id, role_id))

# Save (commit) the changes
# commit operation moved outside the loop to speed up the execution
con.commit()

cur.executescript("""
    SELECT hex(User.name || Course.title || Member.role ) AS X
    FROM User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
""")

# close the file and terminate the cursor
fhand.close()
cur.close()
