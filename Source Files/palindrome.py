def isPalindrome(string):
	return string == string[::-1]







print("Enter A String")
x = input()
pal = isPalindrome(x)

if pal:
	print("It Is A Palindrome")
else:
	print("It Is Not A Palindrome")
