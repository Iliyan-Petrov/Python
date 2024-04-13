import numpy as np

diagonal = np.array([4, 5, 6, 8])

shape = (4, 4)
arr = np.zeros(shape)

np.fill_diagonal(arr, diagonal)

print("2-D array with diagonal [4, 5, 6, 8]:")
print(arr)