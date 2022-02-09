class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []

        for i in nums1:
            if i in nums2:
                idx = nums2.index(i)
                val = nums2.pop(idx)
                answer.append(val)

        return answer
