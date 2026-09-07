class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        
        out = True
        for i in range(len(nums)-1):
            left = i
            right=i+1

            out = out and (nums[left]%2 != nums[right]%2)
        
        return out

