import numpy as np

arr = np.arange(30, 71)

even_arr = arr[arr % 2 == 0]

print(even_arr)
