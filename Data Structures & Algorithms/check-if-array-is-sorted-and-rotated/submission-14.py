class Solution:
    def check(self, nums: List[int]) -> bool:
        #[3,4,5,5,5,1,2]
        #the values only drop once
        n = len(nums)
        drops = 0
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%n]:
                drops+=1

        return drops <= 1
