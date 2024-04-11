class py_solution:
	def reverse_words(self, s): return ' '.join(reversed(s.split()))


resersable_string = input("Please enter a string: ")
print("Reversed String: ")
print(py_solution().reverse_words(resersable_string))
