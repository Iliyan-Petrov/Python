import numpy as np

arr = np.array([[1, 2, 3, 4],
            	[5, 6, 7, 8],
            	[9, 10, 11, 12]])

print("Original array:")
print(arr)

arr_reshaped = np.reshape(arr, (4, 3))

print("Array with new shape:")
print(arr_reshaped)
