class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            else:
                nums_set.add(nums[i])
        return False