class StringProcessor:
	def __init__(self): self.input_string = ""

	def get_String(self): self.input_string = input("Please enter a string: ")

	def print_String(self): print("Upper String: " + self.input_string.upper())

processor = StringProcessor()
processor.get_String()
processor.print_String()
