import self as self


class Rectangle:
	def __init__(self, len, wid): self.length = len; self.width = wid

	def Area(self): print("Rectangle Area: ")
	print(self.length * self.width)


length = int(input("Input Length: "))
width = int(input("Input Width: "))
rec = Rectangle(length,width)
rec.Area()
