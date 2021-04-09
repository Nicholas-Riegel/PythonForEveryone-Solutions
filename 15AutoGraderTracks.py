# It was mostly luck that I solved this. I honestly just hacked away at it until it finally worked. Basically just copying the surrounding code structure to add Genre into everything. It gave me no understanding of the subject matter. This chapter was really poorly designed. Very poor pedagogy. 

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# copied in from assignment 
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = './tracks/Library.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

for entry in all:
    if (lookup(entry, 'Track ID') is None):
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    genre = lookup(entry, 'Genre')  # added

    if name is None or artist is None or album is None or genre is None:  # added "or genre is None"
        continue

    print(name, artist, album, genre, count, rating, length) #added 'genre'

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES(?) ''', (artist, ))

    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))

    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,)) #added

    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, )) #added

    genre_id = cur.fetchone()[0] #added

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', (album, artist_id))

    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))

    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''',
                (name, album_id, genre_id, length, rating, count)) #added genre_id in two places, added a ?

    conn.commit()
