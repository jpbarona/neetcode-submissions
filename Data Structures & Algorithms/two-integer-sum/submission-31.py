class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]

        
        for i in range(len(nums)-1):
            for k in range(i+1, len(nums)):
                if nums[i] + nums[k] == target:
                    return [i,k]
        