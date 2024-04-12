import sqlite3


conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

table_name = 'your_table_name'
query = f'SELECT COUNT(*) FROM {table_name};'
cursor.execute(query)
row_count = cursor.fetchone()[0]
print(f'The number of rows in the table {table_name} is: {row_count}')
cursor.close()
conn.close()
