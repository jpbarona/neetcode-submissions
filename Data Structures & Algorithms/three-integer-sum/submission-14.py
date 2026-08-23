class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        added = defaultdict(bool)
        for i in range(len(nums)):
            num = nums[i]
            target = -num
            l, r = i+1, len(nums)-1
            while l<r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    if not added[(nums[i],nums[l],nums[r])]:
                        solutions.append([nums[i],nums[l],nums[r]])
                        added[(nums[i],nums[l],nums[r])] = True
                    l+=1

        return solutions




