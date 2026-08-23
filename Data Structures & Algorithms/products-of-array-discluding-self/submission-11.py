class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prevProducts = [1] * len(nums)
        forwardProducts = [1] * len(nums)
        output = [0] * len(nums)
        
        for i in range(1, len(nums)):
            prevProducts[i] = prevProducts[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            forwardProducts[i] = forwardProducts[i+1] * nums[i+1]

        for i in range((len(nums))):
            output[i] = (prevProducts[i]  * forwardProducts[i]) 

        return output
