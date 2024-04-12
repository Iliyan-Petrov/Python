import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS students
         	(id INTEGER PRIMARY KEY AUTOINCREMENT,
          	name TEXT,
          	age INTEGER,
          	grade CHAR(2))''')

c.execute("INSERT INTO students (name, age, grade) VALUES ('Alice', 18, 'A+')")
c.execute("INSERT INTO students (name, age, grade) VALUES ('Bob', 19, 'B+')")
c.execute("INSERT INTO students (name, age, grade) VALUES ('Charlie', 20, 'C')")

conn.commit()
conn.close()

def delete_row(row_id):
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	c.execute("DELETE FROM students WHERE id=?", (row_id,))
	conn.commit()
	conn.close()

row_id_to_delete = 2
delete_row(row_id_to_delete)

print(f"Row with id={row_id_to_delete} has been deleted from the table.")
