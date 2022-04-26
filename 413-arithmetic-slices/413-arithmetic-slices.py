class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0

        res = 0
        diff = nums[1] - nums[0]
        curLen = 2
        for i in range(2, len(nums)):
            curDiff = nums[i] - nums[i-1]
            if curDiff == diff:
                curLen += 1
            else:
                res += (curLen - 1) * (curLen - 2) // 2
                curLen = 2
                diff = curDiff
        
        return res + (curLen - 1) * (curLen - 2) // 2