class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prevProducts = [1] * len(nums)
        for i in range(1, len(nums)):
            prevProducts[i] = prevProducts[i-1] * nums[i-1]
        
        forwardProducts = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            forwardProducts[i] = forwardProducts[i+1] * nums[i+1]

        output = [0] * len(nums)
        for i in range((len(nums))):
            left = prevProducts[i] if i>0 else 1
            right = forwardProducts[i] if i < len(nums)-1 else 1
            output[i] = (left * right) 

        return output
