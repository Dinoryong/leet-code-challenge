'''
오름차순 정렬 상태로 주어진다면 binary search를 떠올리자
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            else:
                continue
        return -1