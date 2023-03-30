import sqlite3

conn=sqlite3.connect('database.db')


with open('schema.sql') as r:
    conn.executescript(r.read())


cur=conn.cursor()

cur.execute("INSERT INTO users (first_name, last_name) VALUES (?,?)", ('James', 'Riri'))

cur.execute("INSERT INTO users (first_name, last_name) VALUES(?,?)", ('Wanjiru', 'Maureen'))


conn.commit()
conn.close()