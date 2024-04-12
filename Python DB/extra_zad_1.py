from tabulate import tabulate

headers = ['Name', 'Age', 'City']

data = [
	['John', 28, 'New York'],
	['Alice', 24, 'Los Angeles'],
	['Bob', 32, 'Chicago'],
	['Eve', 29, 'San Francisco'],
	['Charlie', 35, 'Seattle'],
	['Dave', 26, 'Boston'],
	['Frank', 31, 'Houston'],
	['Grace', 27, 'Philadelphia'],
	['Hank', 33, 'Atlanta'],
	['Ivy', 30, 'Miami']
]

table = [headers] + data

print(tabulate(table, headers='firstrow', tablefmt='grid'))
