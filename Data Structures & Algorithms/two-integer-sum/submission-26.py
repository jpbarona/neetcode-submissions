
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



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def copyremove(xs: List[int], i: int):
            return xs[:i] + xs[i+1:]

        targets = {}
        for x in nums:
            targets[x] = target - x

        targets_list = list(targets.values())

        for i in range(len(nums)):
            if targets[nums[i]] in copyremove(nums, i):
                idx_in_nums = nums.index(targets[nums[i]], i+1)
                return [i, idx_in_nums]
        
        return []

# class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
        # def copyremove(xs: List[int], i: int):
            # return xs[:i] + xs[i+1:]

        # targets = {}
        # for x in nums:
            # targets[x] = target - x

        # for i in range(len(nums)):
            # if targets[nums[i]] in copyremove(nums, i):
                # idx_in_nums = nums.index(targets[nums[i]], i + 1)
                # return [i, idx_in_nums]

        # return []
