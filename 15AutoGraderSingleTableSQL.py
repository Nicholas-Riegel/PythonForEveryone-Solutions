import sqlite3

conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages(name VARCHAR(128), age INTEGER)')
cur.execute('DELETE FROM Ages')
cur.execute("INSERT INTO Ages (name, age) VALUES ('Sandie', 37)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Gretchen', 28)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Jana', 18)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Baileigh', 13)")

conn.commit()

conn.close()
