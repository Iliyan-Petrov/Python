import sqlite3

conn = sqlite3.connect('my_database.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS my_table
         	(id INTEGER PRIMARY KEY AUTOINCREMENT,
         	name TEXT,
         	age INTEGER,
         	city TEXT)''')


for i in range(10):
	print(f"Enter data for Record {i + 1}:")
	name = input("Name: ")
	age = int(input("Age: "))
	city = input("City: ")

	c.execute("INSERT INTO my_table (name, age, city) VALUES (?, ?, ?)", (name, age, city))
	print("Record inserted successfully!")

conn.commit()
conn.close()
