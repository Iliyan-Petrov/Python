class BracketChecker:
	def __init__(self):
    	self.stack = []

	def is_valid(self, string):
    	for char in string:
        	if char in '([{':
            	self.stack.append(char)
        	elif char in ')]}':
            	if not self.stack:
                	return False
            	popped_char = self.stack.pop()
            	if (char == ')' and popped_char != '(') or \
               	(char == ']' and popped_char != '[') or \
               	(char == '}' and popped_char != '{'):
                	return False

    	return not self.stack

bracket_checker = BracketChecker()
test_cases = ["()", "()([]{}", "[)", "({[)]", "{{{", "{[()]}", "([{}])"]
for test_case in test_cases:
	if bracket_checker.is_valid(test_case):
    	print(f"{test_case} is valid")
	else:
    	print(f"{test_case} is invalid")