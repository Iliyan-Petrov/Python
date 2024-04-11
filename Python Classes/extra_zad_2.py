class RomanConverter:
	def __init__(self):
    	self.roman_numerals = {
        	'M':1000,
        	'CM':900,
        	'D':500,
        	'CD':400,
        	'C':100,
        	'XC':90,
        	'L':50,
        	'XL':40,
        	'X':10,
        	'IX':9,
        	'V':5,
        	'IV':4,
        	'I':1
    	}

	def convert(self, roman_num):
    	decimal_num = 0
    	previous_value = 0
    	for symbol in roman_num:
        	current_value = self.roman_numerals[symbol]
        	if current_value > previous_value:
            	decimal_num += current_value - 2 * previous_value
        	else:
            	decimal_num += current_value
        	previous_value = current_value
    	return decimal_num

converter = RomanConverter()
roman = input("Please Enter a Roman Numeral: ")
print(converter.convert(roman))
