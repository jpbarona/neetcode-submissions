class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numsSet = set(nums)
        longest = 1
        
        for num in nums:
            #start of sequence
            if (num-1) not in numsSet:
                current = 0
                while ((num + current) in numsSet):
                    current+=1

                longest = max(longest, current)

        return longest

        

            
