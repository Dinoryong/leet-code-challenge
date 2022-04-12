class Solution:
    def maxArea(self, height: List[int]) -> int:
        # M1: Using 2 loops with i from 0 to len and j from i + 1 to len
        # O(n^2) Time Complexity - Time Exceeded for large inputs and O(1) Space Complexity
        
        # M2: Using 2 pointers
        # O(n) Time Complexity and O(1) Space Complexity
        l, r = 0, len(height)-1
        max_area = 0
        while l<r:
            max_area = max((r-l)*min(height[l], height[r]), max_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area