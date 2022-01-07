class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newNums = []
        for num in nums:
            num = num**2
            newNums.append(num)
        
        newNums.sort()
        
        
        return newNums