import pandas as pd

def edit_table_column(table, column_name, old_value, new_value):
	table[column_name] = table[column_name].replace(old_value, new_value)

data = {'Name': ['John', 'Alice', 'Bob', 'Charlie'],
    	'Age': [25, 30, 35, 40],
    	'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

print("Original table:")
print(df)

edit_table_column(df, 'City', 'Chicago', 'San Francisco')

print("\nTable after editing:")
print(df)
