class ArrayPairSum:
	def __init__(self, arr):
    	self.arr = arr

	def find_pairs(self, target_sum):
    	pairs = []
    	seen = {}
    	for i, num in enumerate(self.arr):
        	complement = target_sum - num

        	if complement in seen:
            	pairs.append((seen[complement], i))

        	seen[num] = i

    	return pairs


arr = [2, 3, 5, 7, 8, 11]
target_sum = 10

ap = ArrayPairSum(arr)
pairs = ap.find_pairs(target_sum)

if pairs:
	print("Pairs found:")
	for pair in pairs:
    	print(f"Index {pair[0]} and Index {pair[1]}")
else:
	print("No pairs found.")