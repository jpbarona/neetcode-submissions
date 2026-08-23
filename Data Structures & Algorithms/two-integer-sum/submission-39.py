class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]

        valueMap = {}

        for i, n in enumerate(nums):
            x = target - n
            if x in valueMap:
                return [valueMap[x], i]
            
            valueMap[n] = i

        return []


        