class Solution:
	def moveZeroes(self, nums):
		for i in range(len(nums))[::-1]:
			if nums[i] == 0:
				nums.pop(i)
				nums.append(0)