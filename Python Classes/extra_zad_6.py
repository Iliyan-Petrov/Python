class ThreeSumZero:
	def __init__(self, arr):
    	self.arr = arr

	def find_triplets(self):
    	n = len(self.arr)
    	triplets = []
    	for i in range(n-2):
        	for j in range(i+1, n-1):
            	for k in range(j+1, n):
                	if self.arr[i] + self.arr[j] + self.arr[k] == 0:
                    	triplets.append((self.arr[i], self.arr[j], self.arr[k]))
    	return triplets

arr = [1, -2, 3, -1, 2, -3, 0, 5, -5]
three_sum_zero = ThreeSumZero(arr)
triplets = three_sum_zero.find_triplets()
if triplets:
	print("Triplets whose sum is zero:")
	for triplet in triplets:
    	print(triplet)
else:
	print("No triplets found whose sum is zero.")
