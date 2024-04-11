import math


class Circle:
	def __init__(self, rad): self.radius = rad

	def Area(self): print("Circle Area: "); print(math.pi * self.radius * self.radius)

	def Parameter(self): print("Circle Parameter: "); print(2 * math.pi * self.radius)


radius = int(input("Input Radius: "))
circle = Circle(radius)
circle.Area()
circle.Parameter()
