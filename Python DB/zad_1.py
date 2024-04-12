class Employee:
	def __init__(self, number, name, age, address, salary):
    	self.number = number
    	self.name = name
    	self.age = age
    	self.address = address
    	self.salary = salary

	def __str__(self):
    	return f"Employee Number: {self.number}, Name: {self.name}, Age: {self.age}, Address: {self.address}, Salary: {self.salary}"

class Company:
	def __init__(self):
    	self.employee_records = []

	def add_employee(self, employee):
    	self.employee_records.append(employee)

	def display_records(self):
    	print("Company Table: ")
    	for employee in self.employee_records:
        	print(employee)

	def change_salary(self, emp_number, new_salary):
    	for employee in self.employee_records:
        	if employee.number == emp_number:
            	employee.salary = new_salary
            	break

	def change_address(self, emp_number, new_address):
    	for employee in self.employee_records:
        	if employee.number == emp_number:
            	employee.address = new_address
            	break

	def delete_employee(self, emp_number):
    	for employee in self.employee_records:
        	if employee.number == emp_number:
            	self.employee_records.remove(employee)
            	break

	def find_min_max_avg_salary(self):
    	salaries = [employee.salary for employee in self.employee_records]
    	min_salary = min(salaries)
    	max_salary = max(salaries)
    	avg_salary = sum(salaries) / len(salaries)
    	return min_salary, max_salary, avg_salary

	def count_above_avg_salary(self):
    	avg_salary = self.find_min_max_avg_salary()[2]
    	count = 0
    	for employee in self.employee_records:
        	if employee.salary > avg_salary:
            	count += 1
    	return count

# Create company table
company = Company()

# Add ten employee records
company.add_employee(Employee(1, "John Doe", 30, "123 Main St", 50000))
company.add_employee(Employee(2, "Jane Smith", 25, "456 Elm St", 60000))
company.add_employee(Employee(3, "Bob Johnson", 40, "789 Oak St", 70000))
company.add_employee(Employee(4, "Alice Brown", 35, "234 Maple Ave", 55000))
company.add_employee(Employee(5, "Charlie Green", 28, "567 Cedar Rd", 65000))
company.add_employee(Employee(6, "David White", 32, "890 Pine Dr", 75000))
company.add_employee(Employee(7, "Eve Black", 45, "123 Birch Ln", 80000))
company.add_employee(Employee(8, "Frank Grey", 38, "456 Willow Ct", 90000))
company.add_employee(Employee(9, "Grace Red", 41, "789 Cedar Rd", 100000))
company.add_employee(Employee(10, "Henry Blue", 50, "234 Oak St", 55000))


company.display_records()
company.change_salary(1, 52000)
company.change_address(4, "345 Pine Rd")
company.delete_employee(2)
company.display_records()
min_salary, max_salary, avg_salary = company.find_min_max_avg_salary()
print("Minimum Salary: ", min_salary)
print("Maximum Salary: ", max_salary)
