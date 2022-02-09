class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # {value : index, }
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        print(hashmap)
        # check if hashmap has complement as a key, and simultaneously doesn't have index "i" as a value
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]