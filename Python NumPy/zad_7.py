import numpy as np

array1 = np.array([2, 4, 6, 8, 10])
array2 = np.array([4, 8, 12, 16, 20])

common_values = np.intersect1d(array1, array2)
count = len(common_values)

print("Array 1:", array1)
print("Array 2:", array2)
print("Common Values:", common_values)
print("Count:", count)