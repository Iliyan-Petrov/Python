class RomanNumeralConverter:
	def __init__(self): self.roman_numerals = {
        	1000: 'M',
        	900: 'CM',
        	500: 'D',
        	400: 'CD',
        	100: 'C',
        	90: 'XC',
        	50: 'L',
        	40: 'XL',
        	10: 'X',
        	9: 'IX',
        	5: 'V',
        	4: 'IV',
        	1: 'I'
    	}

	def convert(self, decimal_num):
 roman_num = ''
for value, symbol in self.roman_numerals.items():
 while decimal_num >= value:
	 roman_num += symbol
	 decimal_num -= value
	 return roman_num



converter = RomanNumeralConverter()
number = input("Please enter a number: ")
print("Roman Number: "+converter.convert(int(number)))
