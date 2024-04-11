class SubsetGenerator:
	def __init__(self, nums):
    	self.nums = nums
    	self.subsets = []

	def generate_subsets(self):
    	self._generate([], 0)
    	return self.subsets

	def _generate(self, current_set, index):
    	self.subsets.append(current_set)

    	for i in range(index, len(self.nums)):
        	self._generate(current_set + [self.nums[i]], i + 1)

nums = [4, 5, 6]
subset_gen = SubsetGenerator(nums)
all_subsets = subset_gen.generate_subsets()
print(all_subsets)
