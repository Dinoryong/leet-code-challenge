class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = lambda idx: nums[idx] - nums[0] - idx
        
        n = len(nums)
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)
        
        left, right = 0, n-1
        while left != right:
            pivot = left + (right - left) // 2
            
            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot
            
        return nums[left - 1] + k - missing(left - 1)