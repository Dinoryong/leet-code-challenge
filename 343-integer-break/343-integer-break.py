class Solution:
        def integerBreak(self, n: int) -> int:
            dp = [1]*(n+1)
            for i in range(1, n):
                for j in range(i, n+1, +1):
                    dp[j] = max(dp[j], dp[j-i]*i)
            return dp[n]