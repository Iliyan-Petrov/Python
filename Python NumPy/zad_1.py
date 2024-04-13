import numpy as np

def is_bounded(arr):
	return np.isfinite(arr).all()

# Test with example arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1.0, 2.0, np.inf, 4.0])
arr3 = np.array([1.0, 2.0, np.nan, 4.0])
arr4 = np.array([1.0, 2.0, 3.0, 4.0])

print("arr1 is bounded:", is_bounded(arr1))
print("arr2 is bounded:", is_bounded(arr2))
print("arr3 is bounded:", is_bounded(arr3))
print("arr4 is bounded:", is_bounded(arr4))
