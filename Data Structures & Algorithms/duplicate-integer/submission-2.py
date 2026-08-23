# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)): #n
#             if nums[i] in nums[:i] + nums[i+1:]: #n
#                 return True    
#         return False

#time complexity, n^2

#implement binary search to make nlogn, n for every pass and logn for using the tree to search
#though what would be the time complexity of looking

#set



class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        observed = set()
        for num in nums: #n
            if num in observed:
                return True
            else:
                observed.add(num)
        return False







