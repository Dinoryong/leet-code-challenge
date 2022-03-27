class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
            nums.sort()
            n = len(nums)
            left = 0
            right = n-1 
            rs = 0

            dp = [1]*n

            for i in range(1, n):
                dp[i] = dp[i-1]*2 % (10**9+7)


            while left <= right:
                if nums[left] + nums[right] <= target:
                    rs = (rs + dp[right-left])%(10**9+7)
                    left += 1
                else:
                    right -= 1
            return rs