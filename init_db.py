import sqlite3

conn=sqlite3.connect('database.db')


with open('schema.sql') as r:
    conn.executescript(r.read())


cur=conn.cursor()

cur.execute("INSERT INTO users (title, content) VALUES (?,?)", ('Uno', "This is Riri and I'm so happy to publish my first blog"))

cur.execute("INSERT INTO users (title, content) VALUES(?,?)", ('Nunya', "Ever got irritated by how someone's etiquette?  well, if you have I'm sorry to let you know that is nunya business"))


conn.commit()
conn.close()