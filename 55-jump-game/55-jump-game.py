class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        @cache
        
        def helper(start):
            if nums[start]>=(n-1)-start:
                return True
            
            if start==n-1:
                return True
            
            for i in range(1,nums[start]+1):
                if helper(start+i):
                    return True
            
            
            return False
        
        n=len(nums)
        return helper(0)
        