import sqlite3

conn = sqlite3.connect('notes.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM notes")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
