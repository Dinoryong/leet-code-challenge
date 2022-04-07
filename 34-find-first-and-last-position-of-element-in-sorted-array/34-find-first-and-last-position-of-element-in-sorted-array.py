# from bisect import bisect_left as bl, bisect_right as br
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         ans = [bl(nums, target), br(nums, target)-1]
        
#         if ans[0] == len(nums) or nums[ans[0]] != target:
#             return [-1, -1]
        
#         return ans



class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
          
        # binary search to find the left target
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) //2
            if nums[mid] == target:
                if mid - 1 >= 0 and nums[mid-1] == target:
                    right = mid - 1
                else:
                    start = mid
                    break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # binary search to find the right target
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) //2
            if nums[mid] == target:
                if mid + 1 < len(nums) and nums[mid+1] == target:
                    left = mid + 1
                else:
                    end = mid
                    break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return [start,end]