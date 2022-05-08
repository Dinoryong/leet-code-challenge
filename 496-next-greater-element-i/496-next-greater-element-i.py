class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        save = []
        
        for i in nums1:
            for index, value in enumerate(nums2):
                if value == i:
                    if index == len(nums2)-1:
                        save.append(-1)
                    else:
                        save.append(-1)
                        for j in range(index+1, len(nums2)):
                            if nums2[j] > i:
                                save.pop()
                                save.append(nums2[j])
                                break

        return save