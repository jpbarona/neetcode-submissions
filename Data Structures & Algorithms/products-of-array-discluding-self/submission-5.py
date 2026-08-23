class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1

        zeroIndices = [i for i in range(len(nums)) if nums[i] is 0]
        numZeros = len(zeroIndices)


        for num in nums:
            if num == 0:
                continue
            totalProduct *= num
        
        products = [0] * len(nums)
        if numZeros > 0:
            if numZeros == 1:
                products = [0] * len(nums)
                products[zeroIndices[0]] = totalProduct
            
            #It's better to be imperative.
            if numZeros > 1:
                products = [0] * len(nums)
        else:
            products = [totalProduct] * len(nums)
            for i in range(len(nums)):
                products[i] = int(products[i] / nums[i])

        return products

