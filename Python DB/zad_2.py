import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('contacts.db')
c = conn.cursor()

# Create the contacts table
c.execute('''CREATE TABLE IF NOT EXISTS contacts (
            	id INTEGER PRIMARY KEY AUTOINCREMENT,
            	name TEXT,
            	surname TEXT,
            	age INTEGER,
            	email TEXT UNIQUE,
            	telephone TEXT UNIQUE
        	)''')

# Create the groups table
c.execute('''CREATE TABLE IF NOT EXISTS groups (
            	id INTEGER PRIMARY KEY AUTOINCREMENT,
            	group_name TEXT
        	)''')

# Create the contact_groups table
c.execute('''CREATE TABLE IF NOT EXISTS contact_groups (
            	id INTEGER PRIMARY KEY AUTOINCREMENT,
            	contact_id INTEGER,
            	group_id INTEGER,
            	FOREIGN KEY (contact_id) REFERENCES contacts(id),
            	FOREIGN KEY (group_id) REFERENCES groups(id)
        	)''')

# Insert example data into the contacts table
c.execute("INSERT INTO contacts (name, surname, age, email, telephone) VALUES (?, ?, ?, ?, ?)",
      	('John', 'Doe', 25, 'johndoe@example.com', '1234567890'))
c.execute("INSERT INTO contacts (name, surname, age, email, telephone) VALUES (?, ?, ?, ?, ?)",
      	('Jane', 'Doe', 30, 'janedoe@example.com', '9876543210'))
c.execute("INSERT INTO contacts (name, surname, age, email, telephone) VALUES (?, ?, ?, ?, ?)",
      	('Alice', 'Johnson', 22, 'alice@example.com', '5555555555'))
c.execute("INSERT INTO contacts (name, surname, age, email, telephone) VALUES (?, ?, ?, ?, ?)",
      	('Bob', 'Smith', 40, 'bob@example.com', '1111111111'))
c.execute("INSERT INTO contacts (name, surname, age, email, telephone) VALUES (?, ?, ?, ?, ?)",
      	('Charlie', 'Brown', 35, 'charlie@example.com', '7777777777'))
c.execute("INSERT INTO contacts (name, surname, age, email, telephone) VALUES (?, ?, ?, ?, ?)",
      	('Dave', 'Johnson', 28, 'dave@example.com', '4444444444'))
c.execute("INSERT INTO contacts (name, surname, age, email, telephone) VALUES (?, ?, ?, ?, ?)",
      	('Eve', 'Anderson', 29, 'eve@example.com', '6666666666'))
c.execute("INSERT INTO contacts (name, surname, age, email, telephone) VALUES (?, ?, ?, ?, ?)",
      	('Frank', 'Smith', 32, 'frank@example.com', '2222222222'))
c.execute("INSERT INTO contacts (name, surname, age, email, telephone) VALUES (?, ?, ?, ?, ?)",
      	('Grace', 'Davis', 26, 'grace@example.com', '9999999999'))
c.execute("INSERT INTO contacts (name, surname, age, email, telephone) VALUES (?, ?, ?, ?, ?)",
      	('Hank', 'Wilson', 27, 'hank@example.com', '3333333333'))

# Insert example data into the groups table
c.execute("INSERT INTO groups (group_name) VALUES (?)", ('Family',))
c.execute("INSERT INTO groups (group_name) VALUES (?)", ('Friends',))
c.execute("INSERT INTO groups (group_name) VALUES (?)", ('Colleagues',))

# Insert example data into the contact_groups table
c.execute("INSERT INTO contact_groups (contact_id, group_id) VALUES (?, ?)", (1, 1))
c.execute("INSERT INTO contact_groups (contact_id, group_id) VALUES (?, ?)", (1, 2))
c.execute("INSERT INTO contact_groups (contact_id, group_id) VALUES (?, ?)", (1, 3))
