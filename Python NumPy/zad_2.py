import numpy as np

arr = np.array([1, 2, 3, 4, 5])

if np.all(arr != 0):
	print("None of the elements are zero.")
else:
	print("At least one element is zero.")
