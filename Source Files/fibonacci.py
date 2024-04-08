nums = int(input("Up to how many numbers to display? "))
n1 = 0
n2 = 1
count = 0

if nums <= 0:
   print("Please enter a larger number")
elif nums == 1:
   print("Fibonacci sequence:")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nums:
   	print(n1)
   	nth = n1 + n2
   	n1 = n2
   	n2 = nth
   	count += 1
