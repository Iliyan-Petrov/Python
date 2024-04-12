import sqlite3

conn = sqlite3.connect('my_database.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS entries
         	(id INTEGER PRIMARY KEY, entry TEXT)''')

entries = ["Entry 1", "Entry 2", "Entry 3", "Entry 4", "Entry 5",
       	"Entry 6", "Entry 7", "Entry 8", "Entry 9", "Entry 10"]

for entry in entries:
	c.execute("INSERT INTO entries (entry) VALUES (?)", (entry,))

conn.commit()
conn.close()

print("Entries inserted successfully!")
