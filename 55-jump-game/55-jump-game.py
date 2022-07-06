class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        i = 0
        max_index = nums[i]
        while i < len(nums) and i <= max_index:
            new_index = nums[i]+i
            max_index = max(max_index, new_index)
            i += 1
        if i == len(nums):
            return True
        else:
            return False