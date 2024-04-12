import pandas as pd

table = pd.DataFrame({
	'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
	'Age': [25, 30, 35, 40],
	'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

print("Original Table:")
print(table)

column_name = input("Enter column name to edit: ")
row_index = int(input("Enter row index (0 to {}): ".format(len(table) - 1)))
new_value = input("Enter new value: ")

table.at[row_index, column_name] = new_value

print("\nTable after Editing:")
print(table)
