#Again, I sort of just hacked away at this until I got is. This is a horrible chapter. Horrible pedagogy. 

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# added table Role
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

DROP TABLE IF EXISTS Role; 

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Role (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    role  INTEGER UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json' #deleted '_sample'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]
    role = entry[2] #added

    print((name, title, role)) #added 'role'

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES(?) ''', ( name, ) )
        
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Role (role)
        VALUES ( ? )''', (role, )) # added
    
    cur.execute('SELECT role FROM Role WHERE role = ? ', (role, ))  # added

    role = cur.fetchone()[0]  # added
    
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''', #added '?'
        ( user_id, course_id, role ) ) #added 'role'

    conn.commit()
