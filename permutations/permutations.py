class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(sub_list: List, remain_list: List):
            if len(nums) == len(sub_list):
                result.append(sub_list)
                return
            for i, value in enumerate(remain_list):
                dfs(sub_list+[value], remain_list[:i]+remain_list[i+1:])

        result = []
        dfs([], nums)
        return result