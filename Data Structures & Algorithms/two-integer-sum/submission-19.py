
# """
# [3,4,5,6]
# [4,5,6,3]
# [5,6,3,4]
# [6,3,4,5]

# """

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # def rotate_n(list: List[int], n: int):
#         #     return list[-n] + list[:-n]
        
#         # nums_rotated = {}
#         # nums_rotated[0] = nums

#         # for i in range(1, len(nums)):
#         #     nums_rotated[i] = rotate_n(nums, i)

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]       
#         return None



from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def copyremove(xs: List[int], i: int):
            # Create a copy of the list with the element at index i removed
            return xs[:i] + xs[i+1:]

        targets = {}
        for x in nums:
            targets[x] = target - x

        for i in range(len(nums)):
            complement = targets[nums[i]]
            # Check if the complement exists in the list excluding the current index
            if complement in copyremove(nums, i):
                # Find the index of the complement starting from the next position
                idx_in_nums = nums.index(complement, i + 1)
                return [i, idx_in_nums]
        
        # If no solution is found, return an empty list (though the problem guarantees one solution)
        return []
