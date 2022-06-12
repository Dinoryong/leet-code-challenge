class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (right + left) // 2
            curr = mid * (mid + 1) // 2
            if curr == n:
                return mid
            if n < curr:
                right = mid - 1
            else:
                left = mid + 1
        
        return right